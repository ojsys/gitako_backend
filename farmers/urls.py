from django.urls import path
from .views import RegisterFarmerView, LoginView

urlpatterns = [
    path('register/', RegisterFarmerView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
