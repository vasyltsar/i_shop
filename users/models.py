from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class CustomUserManager(UserManager):
    pass


class User(AbstractUser):
    RETAILER = 'RETAILER'
    WHOLESALER = 'WHOLESALER'
    CLIENT_TYPE_CHOICES = (
        (RETAILER, 'retailer'),
        (WHOLESALER, 'wholesaler')
    )

    email = models.EmailField(null=False, blank=False, db_index=True, unique=True)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    client_type = models.CharField(choices=CLIENT_TYPE_CHOICES, max_length=10, default=RETAILER)
    is_active = models.BooleanField(
        default=False,
        help_text=
        'Designates whether this user should be treated as active. '
        'Unselect this instead of deleting accounts.'

    )

    objects = CustomUserManager()



