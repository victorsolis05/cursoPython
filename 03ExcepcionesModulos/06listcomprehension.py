#List comprehension
print(list(map(lambda x: x * 10, range(10))))
#      return , definimos iterador, iterable. Esto siempre genera una lista
print([x*10 for x in range(10)])

{x*10 for x in range(10)}
(x*10 for x in range(10))

#list conprehesion , con if

resultado = [x*10 for x in range(20) if x%2 == 0]

print(resultado)

resultado = ["Par" if x%2 == 0 else "Non" for x in range(20)]

print(resultado)

#Python Diccionarios

print({"uno": 1})

datos = [
    { "nombre": "alumno1", "edad": 20},
    { "nombre": "alumno2", "edad": 10},
    { "nombre": "alumno3", "edad": 30},
    { "nombre": "alumno4", "edad": 40},
]

print(datos)

nombres = [ x["nombre"] for x in datos]

print(nombres)