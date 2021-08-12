candy_list=["Snikers", "Skittles", "Hershey", "M&Ms", "Kit Kat", "Kinder", "Manzana"]

permitidos = 5

carrito = []
print('''
-------------Bienvenido--------------- 
Elige tus dulces
''')
for i in range(len(candy_list)):
    print(f"({i+1}) {candy_list[i]}")
carrito = []
#TODO: Perdiler al usuario tantos dulces, como permitidos tiene
print("----------------------------------")
x = 0
while x < permitidos:
    op = int(input(f"Dime el número de dulce que deseas: "))
    if op > 0 and op <= len(candy_list):
        carrito.append(candy_list[op - 1])
        x = x + 1
    else:
        print(f"Opción {op} no válida")
        continue

#TODO: Imprimir los dulces que el usuario eligio
print(carrito)

numeros = [10,20,30,40,50]

print(numeros[-1])
print(numeros[2:])
print(numeros[:2])
