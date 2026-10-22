from collections import deque
cola=deque()
#Agregar elementos 
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#Sacar el primer elemento atendido (desencolar)
atendido=cola.popleft()
#mostrar resultados
print("Atendido",atendido)
print("Cola restante",cola)
