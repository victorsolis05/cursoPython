#Ordenada, Indexable, mutable
alumnos=["jose manuel", "leonardo", "victor", "joaquin"]

#Añadir elementos a la lista

alumnos.append("Brayan")

alumnos.insert(1, "Federico")

print(alumnos)

#Conteo de items
print(alumnos.count("Federico"))
#Posicion (index) dentro de la lista
print(alumnos.index("Brayan"))
#Eliminar por conincidencia
alumnos.remove("Brayan")
print(alumnos)

#Eliminar el ultimo item
alumnos.pop()
print(alumnos)

#Invertir el orden
alumnos.reverse()
print(alumnos)

#Ordenar
alumnos.sort()
print(alumnos)

#Cuantos elementos? Tamaño de lista
print(len(alumnos))