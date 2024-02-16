from django.core.mail import send_mail
from custom.models import EmailVerificationToken
import uuid

def send_verification_email(user):
    token = uuid.uuid4().hex
    EmailVerificationToken.objects.create(user=user, token=token)
    verification_url = 'http://localhost:8000/verify-login-email?token=' + token
    send_mail(
        'Verify your email',
        'Please click on the link to verify your email: ' + verification_url,
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
