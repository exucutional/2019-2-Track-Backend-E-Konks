from django.contrib import admin
from chats.models import Chat, Member, Attachment
# Register your models here.

class ChatAdmin(admin.ModelAdmin):
    pass

class MemberAdmin(admin.ModelAdmin):
    pass

class AttachmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Attachment, AttachmentAdmin)
