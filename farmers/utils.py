from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_welcome_email(email, full_name):
    try:
        subject = 'Welcome to Gitako AgricTech'
        message = f'Dear {full_name},\n\nThank you for registering with Gitako AgricTech. We are excited to have you on board!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        logger.info(f'Welcome email sent to {email}')
    except Exception as e:
        logger.error(f'Error sending welcome email to {email}: {e}')
