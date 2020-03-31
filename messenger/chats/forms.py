from django import forms
from chats.models import Chat
from messages.models import Message
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.template import Library

register = Library()

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['topic', 'last_message']

@register.filter(name='data-callback')
class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs = {
        'data-callback': 'recaptchaCallback',
        'data-expired-callback': 'recaptchaExpiredCallback',
        }))
