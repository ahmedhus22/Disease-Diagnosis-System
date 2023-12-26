'''
    loaded_model = load('model.joblib')
    x = pd.Series(['shivering', 'chills',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    x = x.fillna(0)
    for i in range(len(symptoms)):
        weight = df_s['weight'][i]
        x = x.replace(symptoms[i], weight)
    x = x.values.reshape(1, -1)
    print(loaded_model.predict(x))
'''