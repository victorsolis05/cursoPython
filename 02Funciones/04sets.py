#Una dimension, no-ordenados, no-indexados, MUTABLES
#Set
#Valores unicos
alumnos={"jose manuel", "leonardo", "victor", "joaquin"}
print(alumnos)

#añadir items
alumnos.add("Brayan")
alumnos.add("leonardo")
print(alumnos)
#eliminar items en aleatorio
alumnos.pop()
print(alumnos)

#Busqueda y elimnar por coincidencia
if "Brayan" in alumnos:
    alumnos.remove("Brayan")
    print("tengo el alumno en el set")

#inicializar set vacio
prueba=set()
prueba.add("uno")
print(prueba)