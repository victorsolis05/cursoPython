manejador_archivo = open("./02Funciones/texto.txt", mode= "r+", encoding="UTF-8")

print(manejador_archivo)

#for linea in manejador_archivo:
#    print(linea, end="")

print("\n")
print("----------------------------------------------")

inp = manejador_archivo.read()
print(type(inp))
print(inp.split("\n"))

lineaExtra = "\nEsta es una linea de python"

manejador_archivo.writelines(lineaExtra)

manejador_archivo.close()
