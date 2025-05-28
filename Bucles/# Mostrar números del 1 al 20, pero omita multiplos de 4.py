# Mostrar números del 1 al 20, pero omitir los múltiplos de 4

def imprimir_multiplos_con_for():
    for num in range(1,21):
        if num%4==0:
            continue
        print(num)
        
def imprimir_multiplos_con_while(): 
    num=1       
    while num<=20:
        if num%4==0:
            num+=1
            continue
        print(num)
        num+=1
        
opcion = int(input("Elija opción 1 o 2\n1. For\n2. While"))
if opcion == 1:
    imprimir_multiplos_con_for()
elif opcion == 2:
    imprimir_multiplos_con_while()
else: 
    print("Elija una opción valida")
    



        
            