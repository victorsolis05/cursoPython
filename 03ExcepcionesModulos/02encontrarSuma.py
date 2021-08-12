#TODO: Crear el modulo que tenga la funcion "encontrarSuma"


#Supuestos: Recibimos un arreglo (lista) y un numero objetivo
#Vamos a encontrar dos numeros en la lista que sumados nos den el número objetivo
#lista nunca viene vacia
#No se puede repetir el mismo numero
#La lista simepre viene con numeros
#Si no existen dos numeros que regresen la suma del numero objetivo, regresamos vacio
#Return es una lista

#Ejemplos
#input [1,2,3,4,5,6], 7
#return [2,5]

#input: [3,5,-4,8,11,-1,6], 10
#return [-1, 11]

#input: [1,2] , 5
#return []


#import sys
#import os
#functions_path = os.path.join(".", "03ExcepcionesModulos", "functions")
#sys.path.append("./03ExcepcionesModulos/functions")
#sys.path.append(functions_path)
#from encontrar import encontrarSuma

from functions.encontrar import encontrarSuma

print(encontrarSuma([1,2,3,4,5,6,7] , 9))