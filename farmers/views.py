from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Farmer
from .serializers import FarmerSerializer
#from .utils import send_welcome_email
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)


class RegisterFarmerView(generics.CreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        farmer = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        if farmer:
            self.send_welcome_email(farmer)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()

    def send_welcome_email(self, farmer):
        subject = 'Welcome to ELTAN'
        context = {
            'email': farmer.email,
            # Remove any reference to the password here
        }
        html_message = render_to_string('emails/welcome_email.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = farmer.email

        try:
            send_mail(
                subject,
                plain_message,
                from_email,
                [to_email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info(f"Welcome email sent successfully to {to_email}")
        except Exception as e:
            logger.error(f"Error sending welcome email to {to_email}: {str(e)}")


# class RegisterFarmerView(generics.CreateAPIView):
#     queryset = Farmer.objects.all()
#     serializer_class = FarmerSerializer

#     def perform_create(self, serializer):
#         farmer = serializer.save()
        
#         # Send welcome email
#         subject = 'Welcome to ELTAN'
#         html_message = render_to_string('emails/welcome_email.html', {
#                 'email': farmer.email,
#                 'password': farmer.password.cleaned_data['password']  # Be cautious with sending passwords via email
#             })
#         plain_message = strip_tags(html_message)
#         from_email = settings.DEFAULT_FROM_EMAIL
#         to_email = farmer.email
            
#         try:
#             send_mail(
#                 subject,
#                 plain_message,
#                 from_email,
#                 [to_email],
#                 html_message=html_message,
#                 fail_silently=False,
#             )
#             messages.success(request, "Registration successful. Welcome email sent!")
#         except Exception as e:
#             messages.warning(request, "Registration successful, but we couldn't send the welcome email. Please contact support.")
#             # Log the error for debugging
#             print(f"Error sending email: {str(e)}")

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