from django import forms
from .models import Patient, Symptom
# from .models import SymptomChoices

class SymptomForm(forms.Form):
    SYMPTOM_CHOICES_1 = [
        (0, 'itching'),
        (1, 'skin_rash'),
        (2, 'nodal_skin_eruptions'),
        (3, 'continuous_sneezing'),
        (4, 'shivering'),
        (5, 'chills'),
        (6, 'joint_pain'),
        (7, 'stomach_pain'),
    ]
    SYMPTOM_CHOICES_2 = [
        (8, 'acidity'),
        (9, 'ulcers_on_tongue'),
        (10, 'muscle_wasting'),
        (11, 'vomiting'),
        (12, 'burning_micturition'),
        (13, 'spotting_urination'),
        (14, 'fatigue'),
        (15, 'weight_gain'),
    ]
    SYMPTOM_CHOICES_3 = [
        (16, 'anxiety'),
        (17, 'cold_hands_and_feets'),
        (18, 'mood_swings'),
        (19, 'weight_loss'),
        (20, 'restlessness'),
        (21, 'lethargy'),
        (22, 'patches_in_throat'),
        (23, 'irregular_sugar_level'),
    ]
    SYMPTOM_CHOICES_4 = [
        (24, 'cough'),
        (25, 'high_fever'),
        (26, 'sunken_eyes'),
        (27, 'breathlessness'),
        (28, 'sweating'),
        (29, 'dehydration'),
        (30, 'indigestion'),
        (31, 'headache'),
    ]
    SYMPTOM_CHOICES_5 = [
        (32, 'yellowish_skin'),
        (33, 'dark_urine'),
        (34, 'nausea'),
        (35, 'loss_of_appetite'),
        (36, 'pain_behind_the_eyes'),
        (37, 'back_pain'),
        (38, 'constipation'),
        (39, 'abdominal_pain'),
    ]
    SYMPTOM_CHOICES_6 = [
        (40, 'diarrhoea'),
        (41, 'mild_fever'),
        (42, 'yellow_urine'),
        (43, 'yellowing_of_eyes'),
        (44, 'acute_liver_failure'),
        (45, 'fluid_overload'),
        (46, 'swelling_of_stomach'),
        (47, 'swelled_lymph_nodes'),
    ]
    SYMPTOM_CHOICES_7 = [
        (48, 'malaise'),
        (49, 'blurred_and_distorted_vision'),
        (50, 'phlegm'),
        (51, 'throat_irritation'),
        (52, 'redness_of_eyes'),
        (53, 'sinus_pressure'),
        (54, 'runny_nose'),
        (55, 'congestion'),
    ]
    SYMPTOM_CHOICES_8 = [
        (56, 'chest_pain'),
        (57, 'weakness_in_limbs'),
        (58, 'fast_heart_rate'),
        (59, 'pain_during_bowel_movements'),
        (60, 'pain_in_anal_region'),
        (61, 'bloody_stool'),
        (62, 'irritation_in_anus'),
        (63, 'neck_pain'),
    ]
    SYMPTOM_CHOICES_9 = [
        (64, 'dizziness'),
        (65, 'cramps'),
        (66, 'bruising'),
        (67, 'obesity'),
        (68, 'swollen_legs'),
        (69, 'swollen_blood_vessels'),
        (70, 'puffy_face_and_eyes'),
        (71, 'enlarged_thyroid'),
    ]
    SYMPTOM_CHOICES_10 = [
        (72, 'brittle_nails'),
        (73, 'swollen_extremeties'),
        (74, 'excessive_hunger'),
        (75, 'extra_marital_contacts'),
        (76, 'drying_and_tingling_lips'),
        (77, 'slurred_speech'),
        (78, 'knee_pain'),
        (79, 'hip_joint_pain'),
    ]
    SYMPTOM_CHOICES_11 = [
        (80, 'muscle_weakness'),
        (81, 'stiff_neck'),
        (82, 'swelling_joints'),
        (83, 'movement_stiffness'),
        (84, 'spinning_movements'),
        (85, 'loss_of_balance'),
        (86, 'unsteadiness'),
        (87, 'weakness_of_one_body_side'),
    ]
    SYMPTOM_CHOICES_12 = [
        (88, 'loss_of_smell'),
        (89, 'bladder_discomfort'),
        (90, 'foul_smell_ofurine'),
        (91, 'continuous_feel_of_urine'),
        (92, 'passage_of_gases'),
        (93, 'internal_itching'),
        (94, 'toxic_look_(typhos)'),
        (95, 'depression'),
    ]
    SYMPTOM_CHOICES_13 = [
        (96, 'irritability'),
        (97, 'muscle_pain'),
        (98, 'altered_sensorium'),
        (99, 'red_spots_over_body'),
        (100, 'belly_pain'),
        (101, 'abnormal_menstruation'),
        (102, 'dischromic_patches'),
        (103, 'watering_from_eyes'),
        (104, 'increased_appetite'),
    ]
    SYMPTOM_CHOICES_14 = [
        (105, 'polyuria'),
        (106, 'family_history'),
        (107, 'mucoid_sputum'),
        (108, 'rusty_sputum'),
        (109, 'lack_of_concentration'),
        (110, 'visual_disturbances'),
        (111, 'receiving_blood_transfusion'),
        (112, 'receiving_unsterile_injections'),
    ]
    SYMPTOM_CHOICES_15 = [
        (113, 'coma'),
        (114, 'stomach_bleeding'),
        (115, 'distention_of_abdomen'),
        (116, 'history_of_alcohol_consumption'),
        (117, 'blood_in_sputum'),
        (118, 'prominent_veins_on_calf'),
        (119, 'palpitations'),
        (120, 'painful_walking'),
    ]
    SYMPTOM_CHOICES_16 = [
        (121, 'pus_filled_pimples'),
        (122, 'blackheads'),
        (123, 'scurring'),
        (124, 'skin_peeling'),
        (125, 'silver_like_dusting'),
        (126, 'small_dents_in_nails'),
        (127, 'inflammatory_nails'),
        (128, 'blister'),
        (129, 'red_sore_around_nose'),
        (130, 'yellow_crust_ooze'),
        (131, 'prognosis')
    ]
    symptom1 = forms.TextInput()


class SymptomChoicesForm(forms.Form):
    symptoms = forms.CharField(max_length=250)


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'disease', 
            'symptom1', 
            'symptom2',
            'symptom3',
            'symptom4'
        ]
