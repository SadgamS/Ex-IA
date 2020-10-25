# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 23:01:14 2020

@author: Dennis
"""

"""
Repuesta a la Pregunta 1, inciso (c)

"""
 
# Imporatamos pandas y la libreria para graficar 

import pandas as pd
import matplotlib.pyplot as plt

# Leemos los datos con pandas
datos = pd.read_csv("alumnos.csv")

# Mostramos una descripcion de las dos columnas que contiene numeros
print(datos[['edad','notaPromedio']].describe())

# Paleta de los colores personalizado
colors  = ("dodgerblue","salmon", "palevioletred", 
           "steelblue", "seagreen", "plum", 
           "blue", "indigo", "beige", "yellow")

# Grafico de las edades de los alumnos en forma de torta con porcentajes
grafEdad=datos['edad'].value_counts().plot(kind = 'pie', autopct='%1.1f%%' ,pctdistance= .65,
                                  shadow=True, colors=colors, frame=False, center=(0.5,0.5),
                                  textprops={'fontsize':12})
# Modificamos el nombre del eje y
grafEdad.set_ylabel(' ')
# igualmos el tamaño
plt.gca().axis('equal')

# Agregamos un titulo al grafico
plt.title("Edad de los alumnos", weight='bold', size=14)

# Mostramos el grafico
plt.show()

print(" El primer grafico representa que edad tienen los alumnos")
print(" y cuantos tienen esa edad expresado en porcentaje \n")


# Graficamos la cantidad de notas que tienen los alumnos con barras
grafNota=datos['notaPromedio'].value_counts().plot(kind='bar', grid=True)
  
# Ponemos el nombre de los ejes
grafNota.set_ylabel('Cantidad')
grafNota.set_xlabel('Nota Promedio')

# Agregamos un titulo al grafico
plt.title("Nota Promedio de los alumnos", weight='bold', size=14)

# Mostramos el grafico
plt.show()

print(" El segundo grafico representa la nota que tienen los alumnos")
print(" y cuantos tienen esa nota \n")

# Grafico del sexo de los alumnos en forma de torta con porcentajes
grafSexo=datos['sexo'].value_counts().plot(kind = 'pie', autopct='%1.1f%%' ,pctdistance= .65,
                                  shadow=True, colors=colors, frame=False, center=(0.5,0.5),
                                  textprops={'fontsize':12})

# Modificamos el nombre del eje y
grafSexo.set_ylabel(' ')
# igualmos el tamaño
plt.gca().axis('equal')

# Agregamos un titulo al grafico
plt.title("Cantidad de hombres y mujeres", weight='bold', size=14)

# Mostramos el grafico
plt.show()

print(" El tercer grafico representa la cantidad de hombres y mujeres que hay expresado en porcentaje")
print(" Como se puede ver hay mas mujeres pero por una diferencia minima \n")

# Grafico de que departemento son los alumnos en forma de torta con porcentajes
grafDepto=datos['departamento'].value_counts().plot(kind = 'pie', autopct='%1.1f%%' ,pctdistance= .65,
                                  shadow=True, colors=colors, frame=False, center=(0.5,0.5),
                                  textprops={'fontsize':12}, startangle=30)


# Modificamos el nombre del eje y
grafDepto.set_ylabel(' ')
# igualmos el tamaño
plt.gca().axis('equal')

# Agregamos un titulo al grafico
plt.title("Lugar de origen de los alumnos", weight='bold', size=14)

# Mostramos el grafico
plt.show()

print(" El ultimo grafico representa de que departamento vienen los alumnos expresado en porcentaje")
print(" Se puede observar que la mayoria son de La Paz seguido de Santa Cruz y dos departementos solo tiene un estudiante \n")

# Grafico de cantida de hombres y mujeres por departamento
gfDeptSex = datos.groupby(['departamento','sexo'])['sexo'].count().unstack().plot.bar( grid=True, fontsize=12)

# Ponemos el nombre de los ejes
gfDeptSex.set_ylabel('Cantidad')
gfDeptSex.set_xlabel('Departamento')

# Agregamos un titulo al grafico
plt.title("Cantidad de hombres y mujeres por Departamento", weight='bold', size=14)


# Mostramos el grafico
plt.show()

print(" Se puede observar que en Pando y Potosi no hay hombres y los demas tiene una cantidad igual de hombres y mujeres a exepcion de La Paz \n")

# Graficos la nota maxima por departamento y sexo
gfNotseDe=datos.groupby(['departamento','sexo'])['notaPromedio'].max().unstack().plot.bar(grid=True, fontsize=12)

# Ponemos el nombre de los ejes
gfNotseDe.set_ylabel('Nota Promedio')
gfNotseDe.set_xlabel('Departamento')

# Agregamos un titulo al grafico
plt.title("La mejor nota por departamento y sexo", weight='bold', size=14)

# Mostramos el grafico
plt.show()

print(" Se observa a los mejores alumnos por departamento y sexo como se observa el ganador es La Paz en este caso una mujer tiene la mejor nota de todos \n")

# Graficamos la edad por sexo
gfEdsexDep=datos.groupby(['sexo'])['edad'].value_counts().unstack().plot.bar(color=colors, grid=True, fontsize=12)

# Ponemos el nombre de los ejes
gfEdsexDep.set_ylabel('Cantidad')
gfEdsexDep.set_xlabel('Sexo')


# Agregamos un titulo al grafico
plt.title("Edad de alumnos por sexo", weight='bold', size=14)
# Mostramos el grafico
plt.show()

print("Se puede ver que en las mujeres la edad no pasa de los 25 \n")

print("y en los hombres hay mas con 24 años y existe uno con 27,  no hay hombres  con 22 años\n")