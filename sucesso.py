# %%
import pandas as pd
import numpy
import seaborn as sns

df= pd.read_csv('meus_dados_titanic.csv')

print(df.head())

print(df.info())

print(df.describe())

#datatypes dia se é string float int

print(df.dtypes)

#filtro
print(df[df['age'] <=10].head ())

duplicateRows= df[df.duplicated]
print(len(duplicateRows))

print(len(df))
df.drop_duplicates(keep='last',inplace=True)
print(len(df))

#df.dropna(subset=['decki'], inplace =True)

#substituindo Nan por zero
#df.replace(np.nan, '0', inplace=True)

#print(df)

#renomear colunas
df= df.rename(columns={'sex': 'Genero'})

print(df.head(5))

#metodos de ordenação
sorted_df = df.sort_values(by='Genero', ascending=True)
print(sorted_df.head())  

#groupby
grouped_by = df.groupby('age')
print(grouped_by.head())

