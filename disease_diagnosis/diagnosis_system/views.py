from django.shortcuts import render
from .models import Disease, Symptom, Specialist
from django.views.generic import CreateView
from .forms import SymptomChoicesForm
from .diagnosis_prediction import predict_diagnosis


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
            context = {
                'diagnosis': diagnosis,
                'symptoms_list': symptoms_list,
                'additional_message': additional_message
            }
            return render(request, 'diagnosis_system/diagnosis.html', context=context)

    else:
        form = SymptomChoicesForm()
            
    return render(request, 'diagnosis_system/predict.html', context={'form': form})

def diagnosis(request):
    return render(request, 'diagnosis_system/diagnosis.html')
