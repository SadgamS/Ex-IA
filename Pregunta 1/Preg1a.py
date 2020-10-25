# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:36:44 2020

@author: Dennis

"""
"""
Repuesta a la Pregunta 1, inciso (a)

"""
# Importamos la libreia csv para poder sacar los datos del de nuestro archivo .csv
# para asi poder manejar los datos
import csv

"""
Definimos una funcion para obtener los datos del archivo alumnos.csv
para asi guardalos en una lista
"""

def alumnos():
    with open('alumnos.csv', newline='') as csvFile:
        alumno_reader = csv.reader(csvFile) # guardamos los datos
        next(alumno_reader) # hacemos un salto 
        datos=[]
        for fila in alumno_reader: 
            datos.append(fila) # lo guardamos en una lista
    return datos

"""
Funcion para calcular la media recibe dos parametros el primero el conjunto 
de datos y el segundo la columna de donde se calculara la media
"""
def media(datos, columna):
    n = len(datos) # Guardamos la cantidad de filas 
    sumat = 0   
    for fila in datos:   #Recorremos las filas del conjunto de datos 
        if fila[columna] != '': #Preguntamos si el dato no es nulo
            sumat += float(fila[columna])   #Sumamos todos lo datos de la columna
    media = sumat/n #   calculamos la media
    
    return media # Retornamos el valor

"""
Funcion para calcular la desviacion estandar recibe dos parametros el  
primero el conjunto de datos y el segundo la columna de donde se calculara la 
desviacion estandar
"""

def desv_std(datos, columna):
    n = len(datos) # Guardamos la cantidad de filas 
    suma = 0
    med = media(datos, columna) # Guardamos la media de la columna 
    for fila in datos:
        if fila[columna]!='': # Preguntamos si el dato no es nulo
            suma += (float(fila[columna]) - med)**2 # Aplicamos la formula de la desvStd
    var = (suma/(n))**(1/2) # Calcuamos la desviacion estandar 
    
    return var # Retornamos el valor



datos = alumnos()

# Guardamos los datos que necesitamos y hacemos un de redondeo de 6 cifras significativas 
media_nota = round(media(datos,4),6)

desv_nota = round(desv_std(datos,4),6)

media_edad = round(media(datos,5),6)

desv_edad = round(desv_std(datos,5),6)


print("\nEXPLICACION")
print("******* Analisis de la columna NOTA PROMEDIO *******")
print(f"-Media de notas: {media_nota}")
print(f"-Desviacion estandar de: {desv_nota}")
print(f"Concluimos que la nota de un estudiante esta en promedio de: {media_nota}, con una desviacion estandar de: {desv_nota} que causa una tendencia a variar por debajo o encima del valor de la media.")
print("\n******* Analisis de la columna EDAD *******")
print(f"-Media de notas: {media_edad}")
print(f"-Desviacion estandar de: {desv_edad}")
print(f"Concluimos que la edad promedio de los estudiantes es de: {media_edad},  con una desviacion estandar de: {desv_edad} que causa una tendencia a variar por debajo o encima del valor de la media.")
