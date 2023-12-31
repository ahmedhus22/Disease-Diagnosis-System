from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Patient

@receiver(post_save, sender=User)
def create_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(patient=instance)


@receiver(post_save, sender=User)
def save_patient(sender, instance, created, **kwargs):
    instance.patient.save()
