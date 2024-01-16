import pandas as pd
import numpy as np

df_s = pd.read_csv('Symptom-severity.csv')
# df_enc = pd.DataFrame(columns=['encoding'], data=np.arange(133), index=df['Symptom'].to_numpy())
df_enc = pd.DataFrame(data=df_s)
df_enc['weight'] = np.arange(1, 134)
df_enc.to_csv('Symptom-encoding.csv', index=False)