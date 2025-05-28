#Buscar un número en una lista

numeros = [3, 7, 12, 19, 25, 33, 42] #lista predefinida
    
objetivo = int(input("Ingresa el número que querés buscar: ")) 

encontrado = False #bandera, definida antes del bucle, sirve para poder hacer conteos después

contador = 0

for num in numeros:
    contador += 1
    if num == objetivo:
        print(f"Número {objetivo} encontrado en la lista") 
        print(f"Se revisaron {contador} número(s) antes de encontrarlo.")
        encontrado = True
        break

if not encontrado:
    print(f"Número {objetivo} No se encontró en la lista")
    print(f"Se revisaron los {contador} elementos de la lista.")
        
        

   
    

