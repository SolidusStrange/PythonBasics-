"""Un amigo que trabaja en el instituto de estadísticas, le solicita un programa que le permita ordenar
los datos de un arreglo para asi calcular fácilmente la mediana.Usted, con agrado le dice que si, puesto
que le gustan mucho los desafíos. Entonces recuerda que en sus clases de programación, en una prueba salió
el algoritmo de ordenamiento por burbuja y decide hacerlo con el.Este algoritmo ordena los números presentes
en un arreglo de menor a mayor. Funciona comparando cada elemento de la lista con su si-guiente (siempre la
comparación es de solo 2 elementos a la vez). Si los elementos están ordenados avanza una posición. Si los elemen-tos
están al revés intercambia los valores de posición y luego avanza en una posición. Repite el ciclo muchas veces hasta
que termina. A continuación, se presenta un ejemplo de un arreglo si orden y luego el resultado ordenado."""

import random

arreglo = []

for ciclo in range(50):
    aleatorio = random.randint(1, 1000)
    arreglo.append(aleatorio)

print("\nArreglo original")
print(arreglo)

largo_arreglo = len(arreglo)

# Ordenamiento burbuja
for i in range(largo_arreglo - 1):
    for j in range(largo_arreglo - 1 - i):
        if arreglo[j] > arreglo[j + 1]:
            temporal = arreglo[j]
            arreglo[j] = arreglo[j + 1]
            arreglo[j + 1] = temporal

print("\nArreglo ordenado")
print(arreglo)

# Cálculo de la mediana
if largo_arreglo % 2 == 0:
    mediana = (arreglo[largo_arreglo // 2 - 1] + arreglo[largo_arreglo // 2]) / 2
else:
    mediana = arreglo[largo_arreglo // 2]

print("Mediana:", mediana)
