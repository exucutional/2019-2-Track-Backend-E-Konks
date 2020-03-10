from django.urls import path
from users.views import user_detail, user_search
from rest_framework import routers
from users.views import UserViewSet

routers = routers.DefaultRouter()
routers.register('DRF', UserViewSet)

urlpatterns = [
    path('<int:user_id>/', user_detail, name='user'),
    path('search/', user_search, name='user_search'),
]

urlpatterns += routers.urls
