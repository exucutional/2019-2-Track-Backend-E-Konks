from celery import shared_task
from application.celery import app
from django.core.mail import send_mail
from application.settings import EMAIL_HOST_USER
from users.models import User
from datetime import datetime

@app.task()
def add_together(a, b):
    return a + b

@app.task()
def send_email(emails):
    send_mail(
        'Subject here',
        'Here is the message.',
        EMAIL_HOST_USER,
        emails,
        fail_silently=False,
    )

def get_new_users_count():
    return len(User.objects.filter(date_joined__date=datetime.now().date()))

@app.task()
def generate_report():
    report = {
        'new_users_count': get_new_users_count(),
    }
    return report
