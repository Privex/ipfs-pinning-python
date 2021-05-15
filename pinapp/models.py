from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

User: AbstractUser = get_user_model()


class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)


class Pin(models.Model):
    STATUSES = (
        ('pending', 'Pending (Please Wait)'),
        ('pin', 'Pinned'),
        ('del', 'Removed (Unpinned)'),
        ('err', 'Error Occurred'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cid = models.TextField(max_length=255)


