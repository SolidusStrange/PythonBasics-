def mi_resultado():    
    contador = 0
    for fila in range(5):
        for columna in range(5):
            contador += 1
            print(f"{contador} ", end="")
        print()
            
def resultado_chat_gpt():
    contador = 0
    for fila in range(5):
        for columna in range(5):
            contador += 1
            print(str(contador).rjust(2), end=" ")
        print()
                
opcion = int(input("Opcion 1 o 2"))            
if opcion==1:
    mi_resultado()
elif opcion==2:
    resultado_chat_gpt()
