#pedir al usuario un luchador

#TODO: Abrir el csv, u buscar la informacion del luchador

#TODO: hacer una funcion que recive un row( la informacion del luchador)
#generarReporte(x)
#TODO: La funcion generarReprote, calcular el % de victorias, empates y derrotas

#Si el % de victorias es mayor a 50%, entonces el luchador es una superEstrella, Caso contrario es un aspirante
#Return string de la siguiente forma
#====Estadisticas luchador
#Pct Victorias: %
#Pct Derrotas: %
#Pct Empates: %
#Tipo de luchador: Super Estrella
#BONUS : redondear el pct

#TODO: imprimir en pantalla las estadisticas
#BONUS: Generar el .txt con el reporte del luchador
#map, unpacking


import os
import csv
from functions.reportes import generarReporte
from functions.reportes import generarReporteTxt

csvpath = os.path.join(".", "data", "07WWE-Data-2016.csv")
print('''
==============================Bienvenido============================
''')
luchador = input("Escribe el luchador que deseas buscar: ")
encontrado = []
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        if row[0] == luchador:
            encontrado = row
            #print(encontrado)
            break



if  len(encontrado) > 0:
    reporte = generarReporte(encontrado)
    print(reporte)
    generarReporteTxt(encontrado)
else:
    print(f"no se encontro luchador {luchador}")