from django.shortcuts import render, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SymptomChoicesForm, PatientUpdateForm
from .diagnosis_prediction import (
    predict_diagnosis, 
    disease_description, 
    disease_precaution,
    symptoms_choices
)
from users.models import Profile
from django.db.models import Count


def home(request):
    common_disease = Patient.objects.annotate(disease_count=Count('disease')).order_by('-disease_count')[:1][0].disease
    context = {
        'common_disease': common_disease
    }
    return render(request, 'diagnosis_system/home.html', context=context)


def about(request):
    return render(request, 'diagnosis_system/about.html')

@login_required
def diagnosis_predict(request):
    if request.method == 'POST':
        form = SymptomChoicesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            symptoms = cd.get('symptoms')
            symptoms_list = symptoms.split(', ')

            diagnosis, confidence, show_diagnosis, additional_message = predict_diagnosis(symptoms_list)
            description = disease_description(diagnosis)
            precautions = disease_precaution(diagnosis)

            DOCTOR = 2
            doctors = Profile.objects.filter(user_type=DOCTOR)
            specialists__id = []
            for doctor in doctors:
                # diagnosis in doctor.specialities gives NoneType error if specialities is None
                if doctor.specialities is None:
                    continue
                if diagnosis in doctor.specialities:
                    specialists__id.append(doctor.pk)
            recommended_doctors = Profile.objects.filter(pk__in=specialists__id).order_by('-rating')
            
            context = {
                'diagnosis': diagnosis,
                'confidence': confidence,
                'show_diagnosis': show_diagnosis,
                'symptoms_list': symptoms_list,
                'additional_message': additional_message,
                'recommended_doctors': recommended_doctors,
                'description': description,
                'precautions': precautions
            }
            return render(request, 'diagnosis_system/diagnosis.html', context=context)

    else:
        form = SymptomChoicesForm()
        symptoms_unique = symptoms_choices()
        context = {
            'form': form,
            'symptoms_unique': symptoms_unique
        }
            
    return render(request, 'diagnosis_system/predict.html', context=context)


@login_required
def diagnosis(request):
    return render(request, 'diagnosis_system/diagnosis.html')


@login_required
def patient_update(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST , request.FILES, instance=request.user.patient)
        if form.is_valid:
            form.save()
            messages.success(request, f'Your Health Details has been updated!')
            return redirect('patient-update')
        
    else:
        form = PatientUpdateForm(instance=request.user.patient)

    context = {
        'form': form 
    }
    return render(request, 'diagnosis_system/patient_form.html', context)

