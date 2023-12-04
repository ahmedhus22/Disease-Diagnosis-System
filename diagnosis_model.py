import pandas as pd
import sys
import os.path

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import cross_val_score

TEST_SIZE = 0.4

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


def load_data(directory):
    '''
    load data from a dataset csv file into a list of symptoms and diseases.
    return a tuple(evidence, labels)
    dataset taken from kaggle: https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset/data
    '''
    df = pd.read_csv(directory + os.path.sep + 'dataset.csv')

    # clean the data: fix labels and remove null
    cols = df.columns
    data = df[cols].to_numpy().flatten()

    s = pd.Series(data)
    s = s.str.strip()
    s = s.values.reshape(df.shape)

    df = pd.DataFrame(s, columns=df.columns)

    df = df.fillna(0)

    # read Symptom-severity
    df_s = pd.read_csv(directory + os.path.sep + 'Symptom-severity.csv')

    # replace symptom name with severity
    symptoms = df_s['Symptom']
    for i in range(len(symptoms)):
        weight = df_s['weight'][i]
        df = df.replace(symptoms[i], weight)

    # replace 0 for values not in Symptom-severity(unknown severity)
    df = df.replace('dischromic _patches', 0)
    df = df.replace('spotting_ urination', 0)
    df = df.replace('foul_smell_of urine', 0)

    evidence = df.iloc[:,1:].values
    labels = df['Disease'].values

    return (evidence, labels)


def train_model(evidence, labels):
    '''train model using naive bayes classifier'''
    model = CategoricalNB()
    return model.fit(evidence, labels)


if __name__ == '__main__':
    main()
