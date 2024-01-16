import pandas as pd
import numpy as np
import sys
import os.path
from pathlib import Path
from joblib import dump, load

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import cross_val_score

from disease_diagnosis.settings import BASE_DIR

TEST_SIZE = 0.4
FEATURES_SIZE = 17

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage:python diagnosis_model.py directory')

    evidence, label = load_data(sys.argv[1])
    X_train, x_test, Y_train, y_test = train_test_split(
        evidence, label, test_size=TEST_SIZE)
    
    model = train_model(X_train, Y_train)
    predictions = model.predict(x_test)

    # print results
    print(f'Correct: {(y_test == predictions).sum()}')
    print(f'Incorrect: {(y_test != predictions).sum()}')

    kfold = KFold(n_splits=10, shuffle=True, random_state=50)
    DS_train = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
    pd.DataFrame(DS_train,columns=['Scores'])
    print(f'Training Accuracy: {(DS_train.mean()*100.0):.2f}%')

    DS_test = cross_val_score(model, x_test, y_test, cv=kfold, scoring='accuracy')
    pd.DataFrame(DS_test,columns=['Scores'])
    print(f'Testing Accuracy: {(DS_test.mean()*100.0):.2f}%')

    save(model)


def load_data(directory):
    '''
    load data from a dataset csv file into a list of symptoms and diseases.
    return a tuple(evidence, labels)
    dataset taken from kaggle: https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data
    '''
    df = pd.read_csv(directory + os.path.sep + 'dataset.csv')

    # clean the data: fix labels and remove null
    for col in df.columns:
        df[col] = df[col].str.replace('_',' ')

    cols = df.columns
    data = df[cols].to_numpy().flatten()

    s = pd.Series(data)
    s = s.str.strip()
    s = s.values.reshape(df.shape)

    df = pd.DataFrame(s, columns=df.columns)

    df = df.fillna(0)

    # read Symptom-encoding
    df_s = pd.read_csv(directory + os.path.sep + 'Symptom-encoding.csv')
    df_s['Symptom'] = df_s['Symptom'].str.replace('_', ' ')

    # replace symptom name with encoding
    symptoms = df_s['Symptom']
    for i in range(len(symptoms)):
        weight = df_s['weight'][i]
        df = df.replace(symptoms[i], weight)

    # replace 0 for values not in Symptom-encoding(unknown severity)
    #df = df.replace('dischromic  patches', 0)
    #df = df.replace('spotting  urination', 0)
    #df = df.replace('foul smell of urine', 0)

    evidence = df.iloc[:,1:].values
    labels = df['Disease'].values

    return (evidence, labels)


def train_model(evidence, labels):
    '''train model using naive bayes classifier'''
    model = CategoricalNB()
    return model.fit(evidence, labels)


def save(model):
    if not os.path.exists('model.joblib'):
        dump(model, 'model.joblib')


def predict_diagnosis(x):
    '''
    returns a possible diagnosis for some input x
    x should have 17 features ex:['shivering', 'chills', 0, 0, 0 .... (15 0's)]
    '''
    additional_message = ''
    if len(x) < 2:
        additional_message = 'Enter more Symptoms to receive accurate diagnosis'
    x_vector = [i for i in range(FEATURES_SIZE)]
    for i in range(FEATURES_SIZE):
        if i < len(x):
            x_vector[i] = x[i]
        else:
            x_vector[i] = 0
    model = load('model.joblib')
    x = pd.Series(x_vector)
    x = x.fillna(0)

    # read Symptom-encoding
    df_s = pd.read_csv(Path(BASE_DIR, 'diagnosis_system', 'dataset', 'Symptom-encoding.csv'))
    df_s['Symptom'] = df_s['Symptom'].str.replace('_', ' ')
    symptoms_list = df_s['Symptom'].unique()
    for i in range(len(x)):
        if x[i] not in symptoms_list:
            x[i] = 0

    symptoms = df_s['Symptom']
    for i in range(len(symptoms)):
        weight = df_s['weight'][i]
        x = x.replace(symptoms[i], weight)
    x = x.values.reshape(1, -1)
    return model.predict(x)[0], np.max(model.predict_proba(x)), additional_message


def disease_description(disease):
    df_d = pd.read_csv(Path(BASE_DIR, 'diagnosis_system', 'dataset', 'symptom_Description.csv'))
    return df_d[df_d['Disease'] == disease]['Description'].values[0]


def disease_precaution(disease):
    df_p = pd.read_csv(Path(BASE_DIR, 'diagnosis_system', 'dataset', 'symptom_precaution.csv'))
    return df_p[df_p['Disease'] == disease].values[0][1:]


def symptoms_choices():
    df_s = pd.read_csv(Path(BASE_DIR, 'diagnosis_system', 'dataset', 'Symptom-encoding.csv'))
    df_s['Symptom'] = df_s['Symptom'].str.replace('_', ' ')
    return df_s['Symptom'].unique()


if __name__ == '__main__':
    main()
