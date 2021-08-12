import os
import csv

csvpath = os.path.join(".", "data", "05accounting.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    print(csvheader)
    print("===================================")
    for firtname, lastname, ssn in csvreader:
        print(firtname)