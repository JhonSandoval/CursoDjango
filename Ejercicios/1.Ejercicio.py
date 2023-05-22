#Ejercicio 1 ##

# Definir las poblaciones de los municipios
poblacion_bucaramanga = 581000
poblacion_floridablanca = 267000
poblacion_giron = 260000
poblacion_piedecuesta = 163000

# Calcular la población total del AMB
poblacion_total = poblacion_bucaramanga + poblacion_floridablanca + poblacion_giron + poblacion_piedecuesta

# Imprimir el resultado
print("La población total del Área Metropolitana de Bucaramanga es:", poblacion_total)


# Ejercicio 2 ###

# Definir el número de hijos y mascotas por hijo
num_hijos = 3
mascotas_por_hijo = 2

# Calcular el total de mascotas
total_mascotas = num_hijos * mascotas_por_hijo

# Imprimir el resultado
print("Jose tiene un total de", total_mascotas, "mascotas en su hogar.")


#Ejercicio 3

# Definir la población total del AMB
poblacion_total_amb = 1271000

# Calcular el número de mascotas estimado
mascotas_por_personas = 3 / 10
total_mascotas_amb = poblacion_total_amb * mascotas_por_personas

# Imprimir el resultado
print("Se estima que en el Área Metropolitana de Bucaramanga hay", total_mascotas_amb, "mascotas.")


## Reto Ejercicio ##

# Definir la población inicial de mascotas en el AMB
poblacion_inicial_mascotas = 381300

# Definir la tasa de crecimiento anual
tasa_crecimiento = 1.03

# Calcular la población de mascotas en 10 años
poblacion_proyectada_mascotas = poblacion_inicial_mascotas * (1 + tasa_crecimiento/100)**10

# Imprimir el resultado
print("Se proyecta que en 10 años habrá aproximadamente", int(poblacion_proyectada_mascotas), "mascotas en el Área Metropolitana de Bucaramanga.")
