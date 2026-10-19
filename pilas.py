pila = []
print("Paso 1 - Pila inicial:", pila)

for i in range(1, 11):
    pila.append(i)
print("Paso 2 - Pila después de agregar 10 elementos:", pila)

cima = pila[-1]
print("Paso 3 - El elemento en la cima es:", cima)

for i in range(4):
    pila.pop()
print("Paso 4 - Pila después de quitar 4 elementos:", pila)

tamano = len(pila)
esta_vacia = len(pila) == 0
print("Paso 5 - Tamaño de la pila:", tamano)
print("Paso 5 - ¿La pila está vacía?:", esta_vacia)

while len(pila) > 0:
    pila.pop()
    
print("Paso 6 - Pila después de vaciarla por completo:", pila)
print("Estado final - ¿La pila está vacía?:", len(pila) == 0)