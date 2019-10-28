from django.urls import path
from users.views import user_detail
from users.views import user_contacts

urlpatterns = [
    path('user', user_detail, name='user'),
    path('user/contacts', user_contacts, name='user_contacts')
]
