from django.contrib import admin
from .models import ChatHistory

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'query')
    readonly_fields = ('created_at',)
