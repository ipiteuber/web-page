from django.urls import path
from .views import RegisterUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='api_register'),
    path('login/', obtain_auth_token,      name='api_login'),
]