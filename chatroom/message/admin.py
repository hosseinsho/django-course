from django.contrib import admin

# Register your models here.
from .models import Messages,ConversationMember,Conversation


@admin.register(Messages)

class adminMessages(admin.ModelAdmin):
    pass


@admin.register(ConversationMember)
class adminConversationMember(admin.ModelAdmin):
    pass

@admin.register(Conversation)
class adminConversation(admin.ModelAdmin):
    pass