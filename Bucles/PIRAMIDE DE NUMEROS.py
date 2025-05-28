# Número de filas de la pirámide
filas = 5

for fila in range(1, filas + 1):
    # Espacios para centrar la pirámide
    print(" " * (filas - fila), end="")
    
    # Imprimir la primera parte de la secuencia (ascendente)
    for columna in range(1, fila + 1):
        print(columna, end="")
    
    # Imprimir la segunda parte de la secuencia (descendente)
    for columna in range(fila - 1, 0, -1):
        print(columna, end="")
    
    # Salto de línea al final de cada fila
    print()