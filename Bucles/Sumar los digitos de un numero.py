suma, contador = 0, 0

num = int(input("Ingrese un numero. (0 para sumar)"))
while num!=0: #ingrese 0 para parar
    num = int(input("Ingrese un numero. (0 para sumar)"))
    suma += num
    contador += 1
    
print(f"La suma de los {contador} números ingresados es: {suma}")
    
    
    