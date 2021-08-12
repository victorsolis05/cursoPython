def sumados(a,b):
    suma = a + b
    print("estoy sumando")
    return suma


print(sumados(1,5))

#TODO: Funcion qye recibe una lista, esta garantizado que siempre recibimos una lista con numeros
#Calcular el promedio de esos numeros
#Return Numero del promedio

#def promedioList(numeros):
#    total = len(numeros) 
#    if total > 0:
#        suma = 0
#        for x in numeros:
#            suma +=x
#        return suma / len(numeros) 
#    else:
#        return 0;

import sys
import os
functions_path = os.path.join(".", "03ExcepcionesModulos", "functions")
#sys.path.append("./03ExcepcionesModulos/functions")
sys.path.append(functions_path)
from promedio import promedioList

print(promedioList([1,2,3,4,5,6,7,8,9]))
print(promedioList([]))