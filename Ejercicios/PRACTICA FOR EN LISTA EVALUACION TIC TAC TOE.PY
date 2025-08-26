matriz = [
    ["x", 2, 3],
    [4, "x", 6],
    [7, 8, "x"]
]


def revisar_ganador(matriz, simbolo):
    for fila in range(3): #Recorre cada fila.
        temporal = []
        for valor in matriz[fila]:
            temporal.append(valor == simbolo) #temporal se llena con True/False dependiendo si cada valor coincide.
        if all(temporal): #all(temporal) confirma si toda la fila está ocupada por el mismo símbolo.
            print(f"Fila {fila+1} completa con {simbolo}")
            return True

    for columna in range(len(matriz[0])): #Recorre cada columna y verifica igual que con las filas.
        temporal = []
        for valor in range(len(matriz)):
            temporal.append(matriz[valor][columna] == simbolo)
        if all(temporal):
            print(f"Columna {columna+1} completa con {simbolo}")
            return 
        
    # Diagonal izquierda (0,0) (1,1) (2,2)
    
    temporal = []
    for fila in range(len(matriz)):
        temporal.append(matriz[fila][fila] == simbolo)

    if all(temporal):
        print(f"Diagonal izquierda completa con {simbolo}")
        return True

    # Diagonal derecha (0,2) (1,1) (2,0)
    temporal = []
    for fila in range(len(matriz)): #(0.2) (1,1) (2.0)
        temporal.append(matriz[fila][len(matriz) - fila - 1] == simbolo)

    if all(temporal):
        print(f"Diagonal derecha completa con {simbolo}")
        return True

    return False

if revisar_ganador(matriz, "x"):
    print("Juego terminado. Gana el jugador")

elif revisar_ganador(matriz, "o"):
    print("Juego terminado. Gana la maquina")

else:
    print("Empate")