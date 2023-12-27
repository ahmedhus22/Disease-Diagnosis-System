from django.contrib import admin
from .models import Disease
from .models import Symptom
from .models import Specialist

admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Specialist)
