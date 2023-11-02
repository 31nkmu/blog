from django.urls import path
from .views import UserRegistrationAPIView
from . import views

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('login/', views.LoginView.as_view()),
]

