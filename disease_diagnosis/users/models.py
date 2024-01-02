from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django_jsonform.models.fields import JSONField
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    age = models.PositiveSmallIntegerField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Enter a valid phone number')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, null=True)

    PATIENT = 1
    DOCTOR = 2
    USER_TYPE_CHOICES = [
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor')
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    rating = models.IntegerField(default=0, editable=False)

    SPECIALITIES_SCHEMA = {
        'type': 'array',
        'items': {
            'type': 'string',
            'choices': [
                'Fungal infection',
                'Allergy',
                'GERD',
                'Chronic cholestasis',
                'Drug Reaction',
                'Peptic ulcer diseae',
                'AIDS',
                'Diabetes',
                'Gastroenteritis',
                'Bronchial Asthma',
                'Hypertension',
                'Migraine',
                'Cervical spondylosis',
                'Paralysis (brain hemorrhage)',
                'Jaundice',
                'Malaria',
                'Chicken pox',
                'Dengue',
                'Typhoid',
                'hepatitis A',
                'Hepatitis B',
                'Hepatitis C',
                'Hepatitis D',
                'Hepatitis E',
                'Alcoholic hepatitis',
                'Tuberculosis',
                'Common Cold',
                'Pneumonia',
                'Dimorphic hemmorhoids(piles)',
                'Heart attack',
                'Varicose veins',
                'Hypothyroidism',
                'Hyperthyroidism',
                'Hypoglycemia',
                'Osteoarthristis',
                'Arthritis',
                '(vertigo) Paroymsal  Positional Vertigo',
                'Acne',
                'Urinary tract infection',
                'Psoriasis',
                'Impetigo'
            ],
            'widget': 'multiselect'
        }
    }
    specialities = JSONField(schema=SPECIALITIES_SCHEMA, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
