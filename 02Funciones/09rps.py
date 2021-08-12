import random
from colorama import Fore
from colorama import Style

opciones = ["piedra", "papel", "tijera"]

trackCompute = []
trackHumano = []
games = 0
computerWins = 0
humanWins = 0
ties = 0
keepOn = 1
print(f'''
 {Fore.BLUE}========================BIENVENIDO A PIEDRA PAPEL O TIJERA====================={Style.RESET_ALL}

''')
while keepOn == 1:
    # TODO: Logica del juego
    computerChoise = random.choice(opciones)
    print("")
    humanChoise = int(
        input(f"{Fore.RED}Selecciona tu jugada: piedra (0), papel (1), tijera (2) >{Style.RESET_ALL}"))
    humanChoise = opciones[humanChoise]
    print(f'''
       Tu rival eligió: {computerChoise}
       Tu elegiste : {humanChoise}
    ''')
    trackCompute.append(computerChoise)
    trackHumano.append(humanChoise)
    games += 1
    if(computerChoise == humanChoise):
        print("Es un empate")
        ties += 1
    elif computerChoise == "piedra" and humanChoise == "papel":
        print("papel gana a piedra, tu ganas !!")
        humanWins += 1
    elif computerChoise == "tijera" and humanChoise == "piedra":
        print("piedra gana a tijera, tu ganas !!")
        humanWins += 1
    elif computerChoise == "papel" and humanChoise == "tijera":
        print("tijera gana a papel, tu ganas !!")
        humanWins += 1
    elif computerChoise == "papel" and humanChoise == "piedra":
        print("papel gana a piedra, tu pierdes !!")
        computerWins += 1
    elif computerChoise == "piedra" and humanChoise == "tijera":
        print("piedra gana a tijera, tu pierdes !!")
        computerWins += 1
    elif computerChoise == "tijera" and humanChoise == "papel":
        print("tijera gana a papel, tu pierdes !!")
        computerWins += 1
    else:
        print("Error opción no válida")
    # TODO: imprimir estadisticas
    print(f'''
=======================RESULTADOS DE TU DUELO===================================:
        Total de encuentros: {games}
        Veces que te ganaron : {computerWins} ({ (computerWins / games) * 100 } %)
        Que te pusieron: {trackCompute}
        Veces que te la rifaste : {humanWins} ({ (humanWins / games) * 100 } %)
        Que tiraste: {trackHumano}
        Ni a cual irle: {ties}
=================================================================================
    ''')
    keepOn = int(input("¿Continuar tu duelo? (1) Sí (2) No >"))
print("\n")
print("===========================GRACIAS POR JUGAR================================")
