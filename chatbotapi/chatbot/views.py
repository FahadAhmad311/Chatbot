from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import google.generativeai as genai
from datetime import datetime
import logging

from .models import ChatHistory
from .serializers import UserSerializer, ChatHistorySerializer, RegisterSerializer

logger = logging.getLogger(__name__)

# Configure Gemini API
GEMINI_API_KEY = "AIzaSyAI0wlVeB4RJPuNlB8juqQugA1CWK9Q6hw"
GEMINI_MODEL = "gemini-2.5-flash-lite"

try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {e}")


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """User registration endpoint"""
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """User login endpoint"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        }, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get current user profile"""
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    """Chat with Gemini API and save history"""
    user_query = request.data.get('query', '').strip()
    
    if not user_query:
        return Response({'error': 'Query is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    ai_response = None
    error_message = None
    
    try:
        logger.info(f"Processing chat query for user {request.user.id}: {user_query[:50]}")
        
        # Generate response using Gemini API
        logger.info(f"Creating GenerativeModel with {GEMINI_MODEL}")
        model = genai.GenerativeModel(GEMINI_MODEL)
        
        logger.info("Calling generate_content...")
        response = model.generate_content(user_query)
        logger.info(f"Got response object: {type(response)}")
        
        # Extract text from response
        if hasattr(response, 'text') and response.text:
            ai_response = response.text
            logger.info(f"Extracted text: {ai_response[:100]}")
        else:
            ai_response = "I couldn't generate a response. Please try again."
            logger.warning(f"Empty response from Gemini API for query: {user_query}")
            logger.warning(f"Response attributes: {dir(response)}")
    
    except Exception as e:
        logger.exception(f"Gemini API error: {type(e).__name__}: {str(e)}")
        error_message = str(e)
        ai_response = "I'm sorry, I encountered an issue processing your request. Please try again later."
    
    # Save chat history regardless of success or failure
    try:
        logger.info(f"Saving chat history - query length: {len(user_query)}, response length: {len(ai_response) if ai_response else 0}")
        chat_history = ChatHistory.objects.create(
            user=request.user,
            query=user_query,
            response=ai_response or "Error: No response generated"
        )
        logger.info(f"Chat history saved with ID {chat_history.id}")
        
        return Response({
            'id': chat_history.id,
            'query': chat_history.query,
            'response': chat_history.response,
            'created_at': chat_history.created_at
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        logger.exception(f"Failed to save chat history: {type(e).__name__}: {str(e)}")
        return Response(
            {'error': 'Failed to save chat. Please try again.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_history(request):
    """Get user's chat history"""
    history = ChatHistory.objects.filter(user=request.user)
    serializer = ChatHistorySerializer(history, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_chat(request, chat_id):
    """Delete a specific chat from history"""
    try:
        chat = ChatHistory.objects.get(id=chat_id, user=request.user)
        chat.delete()
        return Response({'message': 'Chat deleted successfully'}, status=status.HTTP_200_OK)
    except ChatHistory.DoesNotExist:
        return Response({'error': 'Chat not found'}, status=status.HTTP_404_NOT_FOUND)
