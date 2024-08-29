from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

# def send_welcome_email(email, full_name):
#     try:
#         subject = 'Welcome to Gitako AgricTech'
#         message = render_to_string('emails/welcome_email.html', {
#                 'email': user.email,
#                 'password': form.cleaned_data['password1']  # Be cautious with sending passwords via email
#             })
#         plain_message = strip_tags(message)
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)
#         logger.info(f'Welcome email sent to {email}')
#     except Exception as e:
#         logger.error(f'Error sending welcome email to {email}: {e}')
