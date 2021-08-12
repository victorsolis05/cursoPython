a,b = [1,2]

print(a)
print(b)

#a,b = [1,2, 3]
#a,b,c = [1,2]

a,b = (1,2)

lista_listas = [["uno", "dos"], ["tres", "cuatro"]]
for x in lista_listas:
    a,b = x
    print(a,b)



resultado_map = map(int, ["1", "2", "3", "4", "5"])
print(list(resultado_map))

miLista = [1,2,3,4,5]
resultadoLista = []
for x in miLista:
    resultadoLista.append(x*10)
print(resultadoLista)

def multiplicarDiez(x):
    return x*10

print(list(map(multiplicarDiez, miLista)))


personas = [["Jose", "Barrera"], ["Carlos", "Hidalgo"]]

def concatenarNombreApellido(x):
    nombre, apellido = x
    return f"Señor {nombre} {apellido}"

print(list(map(concatenarNombreApellido, personas)))


print(list(map(lambda x: x*10, [1,2,3,4,5,6])))
