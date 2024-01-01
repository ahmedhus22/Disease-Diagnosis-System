from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='diagnosis_system-home'),
    path('predict/', views.diagnosis_predict, name='diagnosis_system-predict'),
    path('diagnosis/', views.diagnosis, name='diagnosis_system-diagnosis'),
    path('patient/update', views.patient_update, name='patient-update')
]