from django.contrib import admin
from conversation.models import Conversation, ConversationMessage

admin.site.register([Conversation, ConversationMessage])
