from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    PATIENT = 1
    DOCTOR = 2

    USER_CHOICES = [
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor')
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_CHOICES, null=True)
