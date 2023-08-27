from django.urls import path
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path('reg/', UserRegistrationView.as_view()),
    path('login/', CustomAuthToken.as_view()),
]
