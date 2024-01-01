from django.shortcuts import render, redirect
from .models import Patient, Symptom, Specialist
from django.views.generic import CreateView
from .forms import SymptomChoicesForm, PatientUpdateForm
from .diagnosis_prediction import predict_diagnosis, disease_description, disease_precaution
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
                'symptoms_list': symptoms_list,
                'additional_message': additional_message,
                'recommended_doctors': recommended_doctors,
                'description': description,
                'precautions': precautions
            }
            return render(request, 'diagnosis_system/diagnosis.html', context=context)

    else:
        form = SymptomChoicesForm()
            
    return render(request, 'diagnosis_system/predict.html', context={'form': form})

def diagnosis(request):
    return render(request, 'diagnosis_system/diagnosis.html')


def patient_update(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST , request.FILES, instance=request.user.patient)
        if form.is_valid:
            form.save()
            # messages.success(request, f'Your Account has been updated!')
            return redirect('patient-update')
        
    else:
        form = PatientUpdateForm(instance=request.user.patient)

    context = {
        'form': form 
    }
    return render(request, 'diagnosis_system/patient_form.html', context)


class DiagnosisCreateView(CreateView):
    model = Patient
    fields = ['disease', 'symptom1', 'symptom2', 'symptom3', 'symptom4']

    def form_valid(self, form):
        form.instance.patient = self.request.user
        return super().form_valid(form)