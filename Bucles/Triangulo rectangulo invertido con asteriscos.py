def mi_resultado():    
    for fila in range(1, 6):  # fila va de 1 a 5
        for columna in range(1, 6): # columna va de 1 a 5
            if (fila + columna) > 6: # cuando la suma es mayor a 6, se rompe la fila
                break
            print("*", end="") # imprime un asterisco sin salto de línea
        print() # imprime salto de línea al terminar la fila
    
    
def chatgpt():
    for fila in range(1, 6):
        for columna in range(6 - fila):  # El rango de columna se ajusta según la fila
            print("*", end="")
        print()

opcion = int(input("Ingrese opción: (1 o 2)"))
if opcion == 1:
    mi_resultado()
elif opcion ==2:
    chatgpt()
    