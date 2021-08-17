import requests
import json
from config import api_key


def getMovie(pelicula, variable):
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={pelicula}"
    response = requests.get(url).json()
    print(f"{variable} de {pelicula} : {response[variable]}")

getMovie("Alien", "Director")
print("-----------------------------------------")
#print(response)
#print(json.dumps(response, indent=4))

#Director de la pelicula de Alien?

movie = "Alien"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
response = requests.get(url).json()

print(f"Director de la pelicula de Alien? {response['Director']}")

#Clasificación de Gladiador

movie = "Gladiator"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
response = requests.get(url).json()

print(f"Clasificación de Gladiador {response['Rated']}")

#Año en que salio 50 first dates?

movie = "50 First Dates"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
response = requests.get(url).json()

print(f"Año en que salio firs dates? {response['Year']}")


#Escritor de moana

movie = "Moana"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
response = requests.get(url).json()

print(f"Escritor de moana {response['Writer']}")

#Resumen de Sing?

movie = "Sing"
url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie}"
response = requests.get(url).json()

print(f"Resumen de Sing? {response['Plot']}")