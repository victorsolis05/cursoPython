# Supuestos: Recibimos un arreglo (lista) y un numero objetivo
# Vamos a encontrar dos numeros en la lista que sumados nos den el número objetivo
# lista nunca viene vacia
# No se puede repetir el mismo numero
# La lista simepre viene con numeros
# Si no existen dos numeros que regresen la suma del numero objetivo, regresamos vacio
# Return es una lista

def encontrarSuma(lista, objetivo):
    for x in range(len(lista)):
        lista2 = lista[x:]
        for y in range(len(lista2)):
            if (lista[x] + lista2[y]) == objetivo and lista[x] != lista2[y]:
                return [lista[x], lista2[y]]
    return []


def encontrarSuma2(lista, objetivo):
    for i in range(len(lista) - 1):
        numero1 = lista[i]
        for j in range(i + 1, len(lista)):
            numero2 = lista[j]
            if numero1 + numero2 == objetivo:
                return [numero1, numero2]
    return []


if __name__ == "__main__":
    print("Demo funcion")
    print(encontrarSuma([3, 5, -4, 8, 11, -1, 6], 10))
else:
    print("invocamos la funcion desde otro script")
