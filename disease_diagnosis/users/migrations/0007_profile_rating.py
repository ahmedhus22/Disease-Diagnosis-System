# Generated by Django 5.0 on 2024-01-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_specialities'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]