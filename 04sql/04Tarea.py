


import os
import csv
from functions.reportes import generarReporte

csvpath = os.path.join(".", "data", "election_data.txt")

resultados = {}
with open(csvpath, encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    for row in csvreader:
        voterID, county, candidate = row
        if resultados.get(candidate) != None:
           resultados[candidate] += 1
        else:
           resultados[candidate] = 1
        

print(generarReporte(resultados))

