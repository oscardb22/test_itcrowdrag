from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Users(AbstractUser):
    pro = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL
    )

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        ordering = ['first_name']

    def __str__(self):
        return f'{self.username}'
