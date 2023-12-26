# Generated by Django 5.0 on 2023-12-26 18:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[('Fu', 'Fungal infection'), ('All', 'Allergy'), ('GE', 'GERD'), ('Chr', 'Chronic cholestasis'), ('Dr', 'Drug Reaction'), ('Pe', 'Peptic ulcer diseae'), ('AI', 'AIDS'), ('Dia', 'Diabetes'), ('Ga', 'Gastroenteritis'), ('Br', 'Bronchial Asthma'), ('Hyp', 'Hypertension'), ('Mi', 'Migraine'), ('Ce', 'Cervical spondylosis'), ('Pa', 'Paralysis (brain hemorrhage)'), ('Ja', 'Jaundice'), ('Ma', 'Malaria'), ('Ch', 'Chicken pox'), ('De', 'Dengue'), ('Ty', 'Typhoid'), ('HA', 'hepatitis A'), ('HB', 'Hepatitis B'), ('HC', 'Hepatitis C'), ('HD', 'Hepatitis D'), ('HE', 'Hepatitis E'), ('Al', 'Alcoholic hepatitis'), ('Tu', 'Tuberculosis'), ('Co', 'Common Cold'), ('Pn', 'Pneumonia'), ('Di', 'Dimorphic hemmorhoids(piles)'), ('He', 'Heart attack'), ('Va', 'Varicose veins'), ('Hypo', 'Hypothyroidism'), ('Hype', 'Hyperthyroidism'), ('Hy', 'Hypoglycemia'), ('Os', 'Osteoarthristis'), ('Ar', 'Arthritis'), ('Ver', '(vertigo) Paroymsal  Positional Vertigo'), ('Ac', 'Acne'), ('Ur', 'Urinary tract infection'), ('Ps', 'Psoriasis'), ('Im', 'Impetigo')], max_length=10)),
                ('rating', models.IntegerField(default=0, editable=False)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=50)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis_system.diseases')),
            ],
        ),
    ]
