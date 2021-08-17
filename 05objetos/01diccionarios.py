# Arrelo de llave - valor
# no ordenados, no indexados
eng2esp = {"one": "uno", "two": "dos"}

print(len(eng2esp))

print("one" in eng2esp)

vals = list(eng2esp.values())

print("uno" in vals)
eng2esp["two"] = 2
eng2esp["three"] = 3
print(eng2esp)

pelicula = {
    "titulo": "Interstellar",
    "ganancias": {
        "USA": 360,
        "China": 250,
        "UK": 73
    }
}

print(f'La pelicula : {pelicula["titulo"]} tuvo de ganancias {pelicula["ganancias"]["USA"]}')

peliculas = [
    {
        "titulo": "Interstellar",
        "ganancias": {
            "USA": 360,
            "China": 250,
            "UK": 73
        }
    },
    {
        "titulo": "Alien",
        "ganancias": {
            "USA": 36,
            "China": 25,
            "UK": 7
        }
    }
]

for x in peliculas:
    print(x["titulo"])