from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Farmer
from .serializers import FarmerSerializer


class RegisterFarmerView(generics.CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


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