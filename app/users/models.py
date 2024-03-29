from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from .user_services import send_verification_email


class User(AbstractUser):
    """User"""

    image = models.ImageField(
        upload_to='users_images',
        null=True,
        blank=True,
    )
    is_verified_email = models.BooleanField(default=False)
    email = models.EmailField(unique=True)


class EmailVerification(models.Model):
    """Email verification model"""

    code = models.UUIDField(unique=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'{self.__class__.__name__} for {self.user}'

    def send_verification_email(self):
        link = reverse(
            'users:email_verification',
            kwargs={
                'email': self.user.email,
                'code': self.code,
            },
        )

        send_verification_email(
            user=self.user,
            link=link,
        )

    def is_expired(self):
        return now() >= self.expiration
