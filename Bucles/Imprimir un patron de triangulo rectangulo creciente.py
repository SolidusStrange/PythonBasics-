def mi_resultado():
    for fila in range(1, 6):
        for columna in range(5):
            if fila==columna:
                break
            print("*", end="")
        print()
    
def chatgpt():   
    for fila in range(1, 6):  # Desde 1 hasta 5
        for columna in range(fila):  # Imprime tantos * como el número de fila
            print("*", end="")
        print()
        
opcion = int(input("Ingrese opción: (1 o 2)"))
if opcion == 1:
    mi_resultado()
elif opcion ==2:
    chatgpt()