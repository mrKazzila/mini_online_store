import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from .models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(user=user, code=uuid.uuid4(), expiration=expiration)
    record.send_verification_email()