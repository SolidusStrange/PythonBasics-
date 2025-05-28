numeros = []

for num in range(1,11):
    num_ingresado = int(input(f"Ingrese un número {num}/10"))
    numeros.append(num_ingresado)#ingresar a la lista
    
print("Numeros pares")

for i in numeros:
    if i % 2 == 0:
        print(i)
        
        

    