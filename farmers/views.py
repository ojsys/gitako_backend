from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Farmer
from .serializers import FarmerSerializer
from .utils import send_welcome_email
import logging

logger = logging.getLogger(__name__)

class RegisterFarmerView(generics.CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def perform_create(self, serializer):
        farmer = serializer.save()
        # send welcome email
        try:
            send_welcome_email(farmer.email, farmer.full_name)
            logger.info(f'Welcome email sent to {farmer.email}')
        except Exception as e:
            logger.error(f'Error sending welcome email to {farmer.email}: {e}')
            return Response(
                {"detail": "Registration successful, but the welcome email could not be sent."},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"detail": "Registration successful. A welcome email has been sent."},
            status=status.HTTP_201_CREATED
        )

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        farmer = authenticate(request, email=email, password=password)
        if farmer is not None:
            refresh = RefreshToken.for_user(farmer)
            return Response({
                'refresh': str(refresh), 
                'access': str(refresh.access_token)
                })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)