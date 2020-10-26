# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 23:42:49 2020

@author: Dennis
"""

"""
    Respuesta a la pregunta 2
"""

# Importamos pandas
import pandas as pd

# Importamos la librerias para graficar
import seaborn as sns
import matplotlib.pyplot as plt

# Importamos las librerias para el preprocesamiento
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import StandardScaler

# Leemos los datos del dataset
datos =  pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Definimos tres dataframe para guardar los tres metodos
df = pd.DataFrame(datos)

df1 = pd.DataFrame(datos)

df2 = pd.DataFrame(datos)

# hacemos una copia de los datos para hacer el preprocesamiento
copd = pd.DataFrame()

copd = datos[['age','diabetes','high_blood_pressure']]



# Mostrasmos los datos
print(datos)

# Descripcion de los datos que vamos ha usar
print(datos[['age','diabetes','high_blood_pressure']].describe())

"""
    Metodo 1 Escalado estandar
"""


# Creamos una figura con dos sub figuras para graficar
fig, (ax1, ax2)= plt.subplots(ncols=2, figsize=(9,5))

ax1.set_title('Antes de Escalar')

# Graficamos tres columnas para ver el comportamiento 
sns.kdeplot(data=copd, ax=ax1)

# Definimos la variable scaler para hacer el preprocesamiento Standar Scaler 
scaler = StandardScaler()

# Reemplazamos los datos escalados en las mismas columnas,
# El escalado estandar convierte la desviacion estandar sea 1 en todos las columnas que le aplicamos   
df[['age','diabetes','high_blood_pressure']] = scaler.fit_transform(df[['age','diabetes','high_blood_pressure']])

# Graficamos los datos escaldos  
ax2.set_title('Despues de Escalar')
sns.kdeplot(data=df[['age','diabetes','high_blood_pressure']], ax=ax2 )

# guardamos los datos preprocesados en un nuevo archivo
df.to_csv('preproEsc.csv',sep='\t')

# Mostramos la grafica
plt.show()

print(" --- StandarScaler ----")

# Hacemos la descripcion de las columnas que escalamos
print(df[['age','diabetes','high_blood_pressure']].describe())

"""
    Metodo 2 Normalizacion
"""

# Creamos una figura con dos sub figuras para graficar
fig, (ax1, ax2)= plt.subplots(ncols=2, figsize=(9,5))

ax1.set_title('Antes de Normalizar')

# Graficamos tres columnas para ver el comportamiento 
sns.kdeplot(data=copd, ax=ax1)

# Definimos la variable normal para hacer el preprocesamiento de Normalizacion 
normal = Normalizer(norm='l2' , copy=True)
df1[['age','diabetes','high_blood_pressure']] = normal.fit_transform(df1[['age','diabetes','high_blood_pressure']])

# guardamos los datos preprocesados en un nuevo archivo
df1.to_csv('preproNorm.csv',sep='\t')

# Graficamos los datos escaldos  
ax2.set_title('Despues de Normalizar')
sns.kdeplot(data=df1[['age','diabetes','high_blood_pressure']], ax=ax2 )

# Mostramos la grafica
plt.show()

print(" --- Normalizer ----")

# Hacemos la descripcion de las columnas que escalamos
print(df1[['age','diabetes','high_blood_pressure']].describe())

"""
    Metodo 3 Discretizacion
"""

# Creamos una figura con dos sub figuras para graficar
fig, (ax1, ax2)= plt.subplots(ncols=2, figsize=(9,5))

# Graficamos tres columnas para ver el comportamiento 
sns.kdeplot(data=copd,ax=ax1)
ax1.set_title('Antes de Discretizar')
              
# Discretizacion de los datos
discret = KBinsDiscretizer(n_bins=10,encode='ordinal', strategy='uniform')
df2[['age','diabetes','high_blood_pressure']] = discret.fit_transform(df2[['age','diabetes','high_blood_pressure']])

# guardamos los datos preprocesados en un nuevo archivo
df2.to_csv('preproDisc.csv',sep='\t')

# Graficamos los datos discretizados  
ax2.set_title('Despues de Discretizar')
sns.kdeplot(data=df2[['age','diabetes','high_blood_pressure']], ax=ax2 )


# Mostramos la grafica
plt.show()

print(" --- Discretizer ----")

# Hacemos la descripcion de las columnas que escalamos
print(df2[['age','diabetes','high_blood_pressure']].describe())