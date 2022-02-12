import numpy as np
import pandas as pd

data=np.array([['','Col1','Col2'], ['Fila',12,22], ['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

series=pd.Series({
  "Argentina":"Buenos Aires",
  "Chile":"Santiago de Chile",
  "Colombia":"Bogotá",
  "Perú":"Lima"
})

print('Series:')
print(series)

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7,8,9]]))
print('DataFrame:')
print(df)

print('Forma del DataFrame:')
print(df.shape)

print('Altura del DataFrame:')
print(len(df.index))

print('Estadísticas del DataFrame:')
print(df.describe())

print('Media de las columnas DataFrame:')
print(df.mean())

print('Correlación del DataFrame:')
print(df.corr())

print('Conteo de datos del DataFrame:')
print(df.count())

print('Valor más alto de la columna del DataFrame:')
print(df.max())

print('Valor mínimo de la columna del DataFrame:')
print(df.min())

print('Mediana de la columna del DataFrame:')
print(df.median())

print('Desviación estándar de la columna del DataFrame:')
print(df.std())

print('Primera columna del DataFrame:')
print(df[0])

print('Dos columnas del DataFrame:')
print(df[[0, 1]])

print('Valor de la primera fila y última columna del DataFrame:')
print(df.iloc[0][2])


print('Valores de la primera fila del DataFrame:')
print(df.loc[0])

print('Valores de la primera fila del DataFrame:')
print(df.iloc[0,:])

df = pd.read_excel('gestion.xlsx')
# pd.to_csv('gestion-fix.xlsx')

print('Datos nulos en el DataFrame:')
print(df.isnull())

print('Suma datos nulos en el DataFrame:')
print(df.isnull().sum())

print('Reemplazar los valores perdidos por la media:')
print(df.fillna(df.mean ()))