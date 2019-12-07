from django.urls import path
from users.views import user_detail, user_search

urlpatterns = [
    path('<int:user_id>/', user_detail, name='user'),
    path('search/', user_search, name='user_search'),
]
