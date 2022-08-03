from random import randint, shuffle

lista = [1,2,3,4]

lista2 = randint(lista[0],lista[3])
print(f"este es el numero aleatorio {lista2}")

palabras = ['rafael','diana','juan']
shuffle(palabras)
print(f"estas apalabras fueron shuffled {palabras}")

