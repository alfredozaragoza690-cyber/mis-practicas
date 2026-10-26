#Creacion de una matriz 3x3
matriz= [
    [10,20,30]
    [40,50,60]
    [70,80,90]
]
#Acceso a los elemenos matriz [Fila] [columnas]
print (matriz[1][2])#Fila indice 1, columna indice 2
#Modificar elementos 
matriz[0][0]=100
#Recorrer la matriz 
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
        print()

 