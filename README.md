# Disease Diagnosis System
A Disease Diagnosis System based on symptoms. It has 2 types of Users:
- Patients
- Doctors/Specialists

Patients can enter symptoms to be recommended appropriate doctors.
Doctors need to register and get verified by admin to be recommended to patients.

The Webapp is built using Django and scikit-learn is used to perform diagnosis.

Dataset: [Taken from Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)

## Installation
```
    $ pip install -r requirements.txt
```

```
    $ cd disease_diagnosis
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```

## Aim
- To help Patients receive an estimated diagnosis
- Based on that diagnosis recommend some precautions
- Recommend a Doctor to get proper treatment
- Help Doctors manage patients

## How to use the site?
- Home Page shows the most common diagnosis people have received. 
- Patients can register/login to access diagnosis page.
- Get Diagnosed: Enter their symptoms to receive:
    - Diagnosis Prediction.
    - Information about the disease.
    - Precautions they should take.
    - List of Recommended Doctors along with their contact details.
- Save Your Health Conditions:
    - Save the Disease name along with symptoms.
    - It helps gather more data for better diagnosis in future. 
- Doctors can register/login so that they can be recommended.
    - Test Diagnosis: They can test diagnosis prediction to check its accuracy.