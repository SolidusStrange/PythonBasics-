#Ejercicio 1 – Recorrer toda la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Recorre todas las posiciones y muestra:
# Fila x, Columna y → valor

# EJEMPLO ESPERADO: 
# Fila 0, Col 0 → 1
# Fila 0, Col 1 → 2
# Fila 0, Col 2 → 3
# ...

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        valor = matriz[fila][columna]
        print(f"Fila {fila}, Col {columna} → {valor} ")

#Ejercicio 2 – Sumar todos los valores

# Misma matriz de antes. Queremos la suma total de todos los números de la matriz.
# Es decir: 1+2+3+...+9 = 45.

suma = 0
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        valor = matriz[fila][columna]
        suma += valor

print("La suma es:", suma)

#Ejercicio 3 – Encontrar solo números
# Imagina que la matriz tiene mezcla de valores:
# Queremos imprimir solo los números.

matriz_ejercicio = [
    [1, "X", 3],
    ["O", 5, 6],
    [7, 8, "O"]
]

for fila in range(len(matriz_ejercicio)):
    for columna in range(len(matriz_ejercicio[fila])):
        valor = matriz_ejercicio[fila][columna]
        if isinstance(valor, int):
            print(valor)

#EJERCICIO 4 Contar cuántos "X" hay en la matriz

matriz_nueva = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "O"]
]

#Queremos contar cuántas veces aparece "X".
#EL RESULTADO DEBE SER 4

contador_x = 0

for fila in range(len(matriz_nueva)):
    for columna in range(len(matriz_nueva[fila])):
        valor = matriz_nueva[fila][columna]
        if valor == "X":
            contador_x += 1

print("Cantidad de X:", contador_x)

# Ejercicio 5 – Reemplazar todos los "O" por 0
# Dada esta matriz:

matriz = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "O"]
]

#Queremos recorrerla y reemplazar todas las "O" por el número 0.
# La matriz final debería quedar así:

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        valor = matriz[fila][columna]
        if valor == "O":
            matriz[fila][columna] = 0

for fila in matriz:
    print(fila)

#Mini reto:
# ¿Quieres que probemos juntos a imprimirlo todavía más bonito,
# como una cuadrícula (parecido a tu tablero de tres en raya)?

# X | 0 | X
# 0 | X | 0
# X | 0 | 0

print("Mini reto")
for fila in matriz:
    print(" | ".join(str(valor) for valor in fila))