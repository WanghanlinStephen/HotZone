from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Account(models.Model):
    """
    account info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=64, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    work_phone = models.CharField(max_length=32, null=True, blank=True)
    home_phone = models.CharField(max_length=32, null=True, blank=True)

    province = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    area = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - Personal Info'

