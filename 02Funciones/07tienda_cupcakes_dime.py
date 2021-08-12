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

for i in range(len(cupcakes)):
    print(f"({i+1}) {cupcakes[i][0]} - {cupcakes[i][1]} $")
carrito = []


while comprar == "s":
    #TODO pedirle al usuario el producto, y sumar y añadir en el carrito
    op = int(input(f"Dime el número del producto que deseas: "))
    if op > 0 and op <= len(cupcakes):
        carrito.append(cupcakes[op - 1][0])
        total = total + cupcakes[op - 1][1] 
    else:
        print(f"Opción {op} no válida")
    comprar = input("Desea seguir comprando (s) sí (n) n")
print("---------------------")

#TODO: Decirle al cliente sus prodcutos y su total a pagar
print("Tus productos son:")
print(carrito)
print(f"Total a apagar {total}")