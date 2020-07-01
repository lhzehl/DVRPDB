from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image

from .managers import CustomUserManager
from time import time


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user, main field - email
    """
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.profile.username or self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    """
    user profile with additional information, all connection with other models by profile
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField('Profile image', blank=True)
    name = models.CharField('Name', blank=True, max_length=50)
    last_name = models.CharField('Last name', blank=True, max_length=50)
    username = models.CharField('Username', unique=True, blank=True, max_length=150)
    dob = models.DateTimeField('Date of birth', blank=True, null=True)
    new_notification = models.PositiveIntegerField('Number of new notifications', null=True, default=0)

    def __str__(self):
        return f' Profile {self.username or self.user.email}'

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = f'{self.user.email.split("@")[0]}-{int(time())}'
        super().save(*args, **kwargs)
        if not self.image:
            pass
        else:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User`s profiles'
