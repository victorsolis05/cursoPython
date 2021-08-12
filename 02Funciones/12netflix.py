import os
import csv

csvpath = os.path.join(".", "data", "06netflix.csv")
print('''
-------------Bienvenido--------------- 
''')
titulo = input("Escribe el título que deseas buscar: ")
encontrado = []
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    #rint(csvheader)
    #print("===================================")
    for row in csvreader:
        if row[0] == titulo:
            encontrado = row
            #print(encontrado)
            break

    if  len(encontrado) > 0:
        print(f"Rating {encontrado[5]} encontrado de la pelicula {encontrado[0]}")
    else:
        print(f"no se encontro pelicula {titulo}")