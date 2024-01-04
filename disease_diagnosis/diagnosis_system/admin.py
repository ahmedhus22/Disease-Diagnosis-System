from django.contrib import admin
from .models import Patient
from .models import Specialist

admin.site.register(Patient)
admin.site.register(Specialist)
