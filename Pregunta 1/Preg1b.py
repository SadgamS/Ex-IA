# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:19:16 2020

@author: Dennis
"""
"""
Repuesta a la Pregunta 1, inciso (b)

"""
# Importamos las librerias de numpy y pandas
import pandas as pd
import numpy as np

# Leemos los datos con pandas
datos = pd.read_csv("alumnos.csv")

# Imprimos los datos
print('LISTADO DE LOS DATOS')
print(datos)

# Sacamos la media con pandas y redondeamos a 6 cifras sig.
mediaEdad = round(datos['edad'].mean(),6)
mediaNota = round(datos['notaPromedio'].mean(),6)

# Imprimimos la media de la Edad y Nota Promedio
print("\nMEDIA")
print(f"-> Media de notas: {mediaNota}")
print(f"-> Media de edad: {mediaEdad}")

# Convertimos las dos columas en un array de numpy
Notas = np.array(datos['notaPromedio'])
Edad = np.array(datos['edad'])

# Sacamos la desviacion estandar de las dos columnas y redondeamos a 6 cifras sig.
desvStNota = round(Notas.std(),6)

desvStEdad = round(Edad.std(),6)

# Imprimimos la desviacion estandar de la Edad y Nota Promedio
print("\nDESVIACION ESTANDAR")
print(f"-> Desviacion estandar de notas: {desvStNota}")
print(f"-> Desviacion estandar de edad: {desvStEdad }")

#Sacamos la moda con pandas
modaEdad = datos['edad'].mode()
modaNotas = datos['notaPromedio'].mode()
modaDepto = datos['departamento'].mode()

# Imprimimos la moda de la Edad, Nota Promedio y Departamento
print("\nMODA")
print(f"-> Moda de notas: {modaNotas}")
print(f"-> Moda de edades: {modaEdad}")
print(f"-> Moda de de los departamentos: {modaDepto}")


