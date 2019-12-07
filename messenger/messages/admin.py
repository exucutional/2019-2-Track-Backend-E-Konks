from django.contrib import admin
from messages.models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
