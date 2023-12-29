from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age = models.PositiveSmallIntegerField(null=True)

    PATIENT = 1
    DOCTOR = 2
    USER_TYPE_CHOICES = [
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor')
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
