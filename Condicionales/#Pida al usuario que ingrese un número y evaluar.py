#Pida al usuario que ingrese un número entero.

numero = int(input("Ingresa un número entero: "))

#Clasifique el número según las siguientes reglas:
#Si el número es positivo y par, debe imprimir: "El número es positivo y par."
#Si el número es positivo y impar, debe imprimir: "El número es positivo y impar."
#Si el número es negativo y par, debe imprimir: "El número es negativo y par."
#Si el número es negativo y impar, debe imprimir: "El número es negativo y impar."
#Si el número es cero, debe imprimir: "El número es cero."

if numero == 0:
    print("El numero es cero")
else:
    if numero>0 and numero%2!=0: 
        print("El numero es positivo e impar")
    elif numero>0 and numero%2==0: 
        print("El numero es positivo y par")
    elif numero<0 and numero%2==0:
        print("El numero es negativo y par")
    elif numero<0 and numero%2!=0: 
        print("El numero es negativo e impar")
        
        
# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Clasificar el número
if numero == 0:
    print("El número es cero.")
else:
    if numero > 0:
        if numero % 2 == 0:
            print("El número es positivo y par.")
        else:
            print("El número es positivo y impar.")
    else:
        if numero % 2 == 0:
            print("El número es negativo y par.")
        else:
            print("El número es negativo y impar.")
        
        
