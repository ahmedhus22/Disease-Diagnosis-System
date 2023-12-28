from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Disease(models.Model):
    disease = models.CharField(max_length=100)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)


class Symptom(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    symptom = models.CharField(max_length=50)


class Specialist(models.Model):
    DISEASES_CHOICES = [
        ('Fu', 'Fungal infection'),
        ('All', 'Allergy'),
        ('GE', 'GERD'),
        ('Chr', 'Chronic cholestasis'),
        ('Dr', 'Drug Reaction'),
        ('Pe', 'Peptic ulcer diseae'),
        ('AI', 'AIDS'),
        ('Dia', 'Diabetes'),
        ('Ga', 'Gastroenteritis'),
        ('Br', 'Bronchial Asthma'),
        ('Hyp', 'Hypertension'),
        ('Mi', 'Migraine'),
        ('Ce', 'Cervical spondylosis'),
        ('Pa', 'Paralysis (brain hemorrhage)'),
        ('Ja', 'Jaundice'),
        ('Ma', 'Malaria'),
        ('Ch', 'Chicken pox'),
        ('De', 'Dengue'),
        ('Ty', 'Typhoid'),
        ('HA', 'hepatitis A'),
        ('HB', 'Hepatitis B'),
        ('HC', 'Hepatitis C'),
        ('HD', 'Hepatitis D'),
        ('HE', 'Hepatitis E'),
        ('Al', 'Alcoholic hepatitis'),
        ('Tu', 'Tuberculosis'),
        ('Co', 'Common Cold'),
        ('Pn', 'Pneumonia'),
        ('Di', 'Dimorphic hemmorhoids(piles)'),
        ('He', 'Heart attack'),
        ('Va', 'Varicose veins'),
        ('Hypo', 'Hypothyroidism'),
        ('Hype', 'Hyperthyroidism'),
        ('Hy', 'Hypoglycemia'),
        ('Os', 'Osteoarthristis'),
        ('Ar', 'Arthritis'),
        ('Ver', '(vertigo) Paroymsal  Positional Vertigo'),
        ('Ac', 'Acne'),
        ('Ur', 'Urinary tract infection'),
        ('Ps', 'Psoriasis'),
        ('Im', 'Impetigo')
    ]
    speciality = models.CharField(max_length=10, choices=DISEASES_CHOICES)
    specialist = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, editable=False)

