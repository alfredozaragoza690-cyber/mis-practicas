def mostrar_encabezado_escuela(): 
    print("=======================================") 
    print(" Tecnologico de Xicotepec de Juarez ") 
    print("=======================================") 

def obtener_nota_minima_aprobatoria(): 
    return 6.0 

def evaluar_rendimiento(nota_final): 
    if nota_final < 6.0: 
        return "Reprobado" 
    elif nota_final >= 7.0 and nota_final <= 9.4: 
        return "Aprobado" 
    else: 
        return "Excelente" 

def calcular_promedio_ponderado(nota_examenes, nota_tareas): 
    calificacion_final = (nota_examenes * 0.70) + (nota_tareas * 0.30) 
    return calificacion_final 

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas): 
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas) 
    nota_minima = obtener_nota_minima_aprobatoria() 
    estado = evaluar_rendimiento(nota_final) 
    
    if nota_final < nota_minima: 
        extraordinario = "Claro que si, ponte a estudiar" 
    else: 
        extraordinario = "No, Felicidades" 
        
    print("---------------------------------------") 
    print(f"Alumno: {nombre_alumno}") 
    print(f"Nota Final Ponderada: {nota_final:.2f}") 
    print(f"Estado Académico: {estado}") 
    print(f"¿Necesita examen extraordinario?: {extraordinario}") 
    print("---------------------------------------") 

mostrar_encabezado_escuela() 
generar_boleta("Alfredo", 8.5, 9.0) 
generar_boleta("Aaron", 5.0, 6.0) 
generar_boleta("Jaime", 10.0, 9.5)
