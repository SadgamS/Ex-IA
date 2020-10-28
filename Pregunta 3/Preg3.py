# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:13:36 2020

@author: Dennis
"""
"""
    Respuesta a la pregunta 3
"""

# Importamos pandas
import pandas as pd

# Importamos el Arbol de Decision de sklearn 
from sklearn.tree import DecisionTreeClassifier
# Importamos la funcion train_test_split para dividir los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split 
# Importamos la matriz confusion y accuracy_score el cual calculara la precision del arbol 
from sklearn.metrics import confusion_matrix, accuracy_score
# para graficar
import matplotlib.pyplot as plt

# Librerias para graficar el arbol
from sklearn.tree import export_graphviz
from pydotplus import graph_from_dot_data

# librerias para graficar la matriz de confusion 
from mlxtend.plotting import plot_confusion_matrix


# Cargamos los datos 
datos = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# Escogemos las columnas independientes que usaremos para el arbol 
columnas = ['ejection_fraction','serum_creatinine','time']

# Guardamos los datos en x
x = datos[columnas]

# Guardamos la variable dependiente en y
y = datos['DEATH_EVENT']


# hacemos la division de los datos para entrenamiento y prueba
# Usamos el 80% de los datos para entrenamiento y el 20% para pruebas  
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# Creamos el arbol de decision con una altura maxima de nodos igual a 4 y lo clasifica de la mejor manera posible
# y usa el critero de entriopia para medir la calidad 
arbolDec = DecisionTreeClassifier(max_depth=4,random_state=0, criterion='entropy')

# Construimos el arbol con los valores de entrenamiento
arbolDec = arbolDec.fit(X_train,y_train)

# Hacemos la prediccion con los valores de x de prueba
y_pred = arbolDec.predict(X_test)

# guardamos la precision del arbol 
dt_acc = accuracy_score(y_test, y_pred)

# vemos el porcentaje de la prediccion
print("Accuracy:", round(100*dt_acc,0),'%')


cm = confusion_matrix(y_test, y_pred)

print(cm)

# graficamos la matriz de confusion
plt.figure()

plot_confusion_matrix(cm, figsize=(12,8), hide_ticks=True, cmap=plt.cm.Blues)
plt.title("Arbol de Decision - Matriz de Confusion ", fontsize=16)
plt.xticks(range(2), ["Corazón no fallido","Corazón fallido"], fontsize=16)
plt.yticks(range(2), ["Corazón no fallido","Corazón fallido"], fontsize=16)
plt.show()



dot_data = export_graphviz(arbolDec,feature_names=columnas, class_names=['No Murio del Corazon', 'Murio del Corazon'])   

graph = graph_from_dot_data(dot_data)

graph.write_png('Arbol.png')
