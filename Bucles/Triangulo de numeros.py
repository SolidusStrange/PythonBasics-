
def miresultado():    
    for fila in range(1,6):
        for columna in range(1,6):
            print(columna, end="") 
            if fila==columna:
                break     
        print()
        
def chatgpt():   
    for fila in range(1, 6):
        for columna in range(1, fila + 1):
            print(columna, end="")
        print()
        
opcion = int(input("Opcion 1 o 2"))            
if opcion==1:
    miresultado()
elif opcion==2:
    chatgpt()