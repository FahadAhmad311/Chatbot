#!/usr/bin/env python
"""Test script to verify chat endpoint"""
import sys
import os

# Setup Django
sys.path.insert(0, 'd:\\Chatbotnew\\chatbotapi')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbotapi.settings')

import django
django.setup()

# Now import Django/API dependencies
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from chatbot.models import ChatHistory
import google.generativeai as genai
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

print("\n=== Testing Chat Endpoint Components ===\n")

# 1. Test genai
print("[1] Testing genai import and configuration...")
try:
    genai.configure(api_key="AIzaSyDxV80MYlt6BJ8hJrQuVvIjSHHUlZcfzAYs")
    print("  ✓ genai.configure() succeeded")
except Exception as e:
    print(f"  ✗ FAILED: {e}")
    sys.exit(1)

# 2. Test model creation
print("[2] Testing GenerativeModel creation...")
try:
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    print("  ✓ GenerativeModel created")
except Exception as e:
    print(f"  ✗ FAILED: {e}")
    sys.exit(1)

# 3. Test content generation
print("[3] Testing generate_content()...")
try:
    response = model.generate_content("Say 'working' in exactly one word")
    print(f"  ✓ generate_content() succeeded")
    print(f"  - Response type: {type(response).__name__}")
    print(f"  - Has .text: {hasattr(response, 'text')}")
    if hasattr(response, 'text'):
        print(f"  - Text content: '{response.text}'")
    else:
        print(f"  - Response attributes: {[a for a in dir(response) if not a.startswith('_')]}")
except Exception as e:
    print(f"  ✗ FAILED: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# 4. Test user creation
print("[4] Testing user and token creation...")
try:
    user, created = User.objects.get_or_create(
        username='testchat',
        defaults={'email': 'testchat@test.com'}
    )
    token, created = Token.objects.get_or_create(user=user)
    print(f"  ✓ User '{user.username}' (ID: {user.id}) and token exist")
except Exception as e:
    print(f"  ✗ FAILED: {e}")
    sys.exit(1)

# 5. Test chat history save
print("[5] Testing ChatHistory save...")
try:
    chat = ChatHistory.objects.create(
        user=user,
        query="Test query",
        response="Test response"
    )
    print(f"  ✓ ChatHistory saved (ID: {chat.id})")
    chat.delete()
except Exception as e:
    print(f"  ✗ FAILED: {e}")
    sys.exit(1)

print("\n✓ All component tests passed!")
print("\nYou can now test the endpoint by making a POST request to:")
print("  POST http://localhost:8000/api/chat/")
print("  Authorization: Token " + token.key)
print("  Body: {\"query\": \"Hello, how are you?\"}")
