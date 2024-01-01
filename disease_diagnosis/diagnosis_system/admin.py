from django.contrib import admin
from .models import Patient
from .models import Symptom
from .models import Specialist

admin.site.register(Patient)
admin.site.register(Symptom)
admin.site.register(Specialist)
