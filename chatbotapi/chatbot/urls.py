from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.user_profile, name='user-profile'),
    path('chat/', views.chat, name='chat'),
    path('history/', views.chat_history, name='chat-history'),
    path('history/<int:chat_id>/', views.delete_chat, name='delete-chat'),
]
