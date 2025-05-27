from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None 
    email = models.EmailField(unique=True, verbose_name=_('email_address'))
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name=_('role'))
    first_name = models.CharField(max_length=50, verbose_name=_('first_name'), **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name=_('last_name'), **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name=_('phone_number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self): 
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['id']
