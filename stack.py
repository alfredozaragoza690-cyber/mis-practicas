historial_navegacion =[]
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")

print("Historial Cargado: ", historial_navegacion)
#OPERACION CIMA  (top/pek)

pagina_actual=historial_navegacion[-1]
print("Pagina actual en pantalla: ",pagina_actual)

#OPERACION DE DESAPILAR (POP)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de: ", pagina_cerrada)
print("historial despues de presionar 'atras':".historial_navegacion)

#TAMAÑO PILA
total_paginas=len(historial_navegacion)
print("Paginas previas guardadas:",total_paginas)

#OPERACION VACIA (EMPY)
sin_paginas=len(historial_navegacion)==0
print("¿El historial estta vacio?",sin_paginas)


