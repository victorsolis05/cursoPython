#TODO: Funcion qye recibe una lista, esta garantizado que siempre recibimos una lista con numeros
#Calcular el promedio de esos numeros
#Return Numero del promedio

def promedioList(numeros):
    total = len(numeros) 
    if total > 0:
        suma = 0
        for x in numeros:
            suma +=x
        return suma / len(numeros) 
    else:
        return 0

if __name__=="__main__":
    print("Demo funcion")
    print(promedioList([5,6,7,8,9]))
else:
    print("invocamos la funcion desde otro script")