lista = [1,2,3,4]

print(type(lista))
lista.append(5)
print(lista)

for i,j in enumerate(lista):
    print(f"Posición {i} elemento {j}")

print(f"La lista tiene una longitud de {len(lista)} elementos")