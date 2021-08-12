x = 5

if 2 * x > 10:
    print("Funciona")
else:
    print("Necesitas más trabajo")


x = 5
if len("Gato") < x:
    print("Funciona")
else:
    print("No")

x = 2
y = 5

if (x ** 2 >= y) and (y ** 2 < 26):
    print("Bien!")
else:
    print("Ohhh")

altura = 66
edad = 16
permiso_de_adulto = True
if altura > 70 and edad >= 18:
    print("Puede subir a todos los juegos")
elif altura > 65 and edad >= 18:
    print("Puede subir a juegos moderados")
elif altura > 60 and edad >= 18:
    print("Puede subir a juegos básicos")
#elif (altura > 50 and edad >= 18) or (permiso_de_adulto==True and altura > 50):
elif (altura > 50 and edad >= 18) or (permiso_de_adulto and altura > 50):
    print("Puede entrar a los carritos chocones")
else:
    print("Solo juegos para niños")