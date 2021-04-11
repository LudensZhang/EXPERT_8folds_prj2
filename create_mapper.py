import pandas as pd


df_1 = pd.read_csv('class1.csv')
df_2 = pd.read_csv('class2.csv')
df_3 = pd.read_csv('class3.csv')

df = pd.concat([df_1, df_2, df_3], ignore_index=1)
df = df.drop(df.columns[0], axis=1)
df.to_csv('mapper.csv')