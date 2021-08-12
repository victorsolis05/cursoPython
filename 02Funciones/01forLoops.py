print(range(5))
print(list(range(5)))
print(range(10,20))
print(list(range(10,20)))

mi_lista = [10,20,30,40] #Colecckion de items, de una dimesion

quesos = ["Cheddar", "Edam", "Gouda"]

otra_lista = ["spam", 2.0, 6, [10,20], quesos]

#La lista es una coleccion ORDENADA, INDEXADA, MUTABLE
mi_lista[2]= 100
print(otra_lista[3][1])

print("abcde"[1])

print(range(5)[2])

#Listas,string y range() son iterables

for x in "abcde":
    print(x)

for x in quesos:
    print(f"Queso: {x}")

for x in range(5):
    print(x*10);