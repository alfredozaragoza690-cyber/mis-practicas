from collections import deque
import time 
cola_reproduccuin=deque()
#Agregar elementos de reproduccion
cola_reproduccuin.append("Mochila Azul")
cola_reproduccuin.append("Aerolinea Carrillo")
cola_reproduccuin.append("La calacabaza")
#Mostrar las canciones en espera
print("Canciones en espera:")
for cancion in cola_reproduccuin:
    print("_",cancion)
print("Iniciando Reproduccion") 
    #Descolar
while cola_reproduccuin:
    cancion_actual=cola_reproduccuin.popleft()
    print(f"Sonando ahora: {cancion_actual}")
    time.sleep(1) #Simula la duracion del tema 
    print("Finalizo",cancion_actual)
#Muestra cuantas canciones quedan en la cola 
print(f"(Quedan:{len(cola_reproduccuin)})")
print(f"La cola de reproduccion ha finalizado ")
