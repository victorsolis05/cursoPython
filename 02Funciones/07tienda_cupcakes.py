pastelitos = ["Durazno", "Manzana", "Platano", "Fresa", "Blueberry", "Manteconcha"]
precios = [10,10,10,15,15,15]

cupcakes = [ ["Durazno", 10], ["Manzana", 10], ["Platano", 10], ["Fresa", 15], ["Blueberry", 15], ["Manteconcha", 15]];


comprar = "s"

carrito  = []

total = 0
#TODO: Mensaje de bienvenida y menú
print('''
-------------Bienvenido--------------- 
Elige tus productos
''')
#for i in range(len(pastelitos)):
#    print(f"({i+1}) {pastelitos[i]} - {precios[i]} $")
#carrito = []

#for x in zip(pastelitos, precios):
#   print(f"({pastelitos.index(x)}) Pastel: {x[0]} , precio: {x[1]} $")

#for x,y in zip(pastelitos, precios):
#    print(f"({pastelitos.index(x) + 1}) Pastel: {x} , precio: {y} $")

#for x,y in enumerate(zip(pastelitos, precios)):
#    print(f"({pastelitos.index(x) + 1}) Pastel: {x} , precio: {y} $")

for x,y in enumerate(zip(pastelitos, precios)):
    print(f"({x +1}) {y[0]} | $ {y[1]} $")

carrito = []

while comprar == "s":
    #TODO pedirle al usuario el producto, y sumar y añadir en el carrito
    op = input(f"Dime el número del producto que deseas: ")
    if op.isnumeric() and  int(op) > 0 and  int(op) <= len(pastelitos):
        op = int(op)
        carrito.append(pastelitos[op - 1])
        total = total + precios[op - 1]
    else:
        print(f"Opción {op} no válida")
    comprar = input("Desea seguir comprando (s) sí (n) n")
print("---------------------")

#TODO: Decirle al cliente sus prodcutos y su total a pagar
print("Tus productos son:")
print(carrito)
print(f"Total a apagar {total}")