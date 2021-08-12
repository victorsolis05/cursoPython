#modulos
import random
prueba = random

prueba.seed(5)

print(prueba.random())

print(prueba.randrange(0, 10))

prueba2 = random

print(prueba2.randrange(0, 10))

miLista = ["a", "b", "c", "d", "e"]

print(random.choice(miLista))
print(random.choice("abcde"))

from random import choice as elegir

print(elegir("abcdef"))