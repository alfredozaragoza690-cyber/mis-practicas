nombres = []
nombres_totales = [
    "1.Alfredo","2.Raul","3.Ponchito","4.Ricardo","5.Zaid","6.Aaron","7.Brian","8.Beto","9.Jaime","10.Francisco"
]

for name in nombres_totales:
    nombres.append(name)

print("nombres en la pila:", nombres_totales)
print("Ultimo nombre en la pila:", nombres[-1])

primera_salida = nombres.pop()
print("Salida del primer nombre: ", primera_salida)

segunda_salida = nombres.pop()
print("Salida del segundo nombre:", segunda_salida)

tercera_salida = nombres.pop()
print("Salida del tercer nombre:", tercera_salida)

cuarta_salida = nombres.pop()
print("Salida del  cuarto nombre:", cuarta_salida)

print("La lista despues de quitar los nombres es: ", nombres)
nombres_totales = len(nombres)
print("Cantidad de nombres que quedan:", nombres_totales)

if nombres_totales == 0:
    print("La pila esta vacia ")
else:
    print("La pila todavia tiene elementos")

while len(nombres) > 0:
    nombres.pop()

print("La pila después del Paso 6 esta vacia:", nombres)