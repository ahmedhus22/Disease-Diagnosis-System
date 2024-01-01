from django.shortcuts import render
from .models import Disease, Symptom, Specialist
from django.views.generic import CreateView
from .forms import SymptomChoicesForm
from .diagnosis_prediction import predict_diagnosis, disease_description
from users.models import Profile


def home(request):
    return render(request, 'diagnosis_system/home.html')


def diagnosis_predict(request):
    if request.method == 'POST':
        form = SymptomChoicesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            symptoms = cd.get('symptoms')
            symptoms_list = symptoms.split(', ')

            diagnosis, additional_message = predict_diagnosis(symptoms_list)
            description = disease_description(diagnosis)
            
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
                'symptoms_list': symptoms_list,
                'additional_message': additional_message,
                'recommended_doctors': recommended_doctors,
                'description': description
            }
            return render(request, 'diagnosis_system/diagnosis.html', context=context)

    else:
        form = SymptomChoicesForm()
            
    return render(request, 'diagnosis_system/predict.html', context={'form': form})

def diagnosis(request):
    return render(request, 'diagnosis_system/diagnosis.html')
