import datetime
def saludar ():
    print ("Hola, bienvenidos ")
saludar ()

def mostrar_hora ():
        hora_actual=datetime.datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual es:{hora_actual}")
mostrar_hora()

def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado=calcular_area_triangulo(10,5)
print(f"El area del triangulo es:{resultado}")

def saludar_persona(nombre,edad):
    print(f"Hola {nombre}, tienes {edad}")
    saludar_persona("Alfredo",21)
#------------------Ejemplos------------------

def despedirse():
    print("Adios, Vaquero ")
despedirse()

def mostrar_fecha():
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"La fecha de hoy es: {fecha_actual}")
mostrar_fecha()

def calcular_area_rectangulo(base,altura):
    area = base * altura
    return area
resultado_area = calcular_area_rectangulo(8, 4)
print(f"El area del rectangulo es: {resultado_area}")

def sumar_numeros(num1,num2):
    suma = num1 + num2
    return suma
resultado_suma = sumar_numeros(15, 20)
print(f"El resultado de la suma es: {resultado_suma}")

 
