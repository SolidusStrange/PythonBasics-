#Sumar números hasta que el usuario escriba "fin"

suma = 0
while True:
    entrada = input("Ingresa un numero o 'fin'  para terminar: ")

    if entrada == "fin":
        break
    
    try:
        numero = float(entrada) #intentamos convertir la entrada a un numero
        suma += numero #sumamos el numero al total
    except ValueError:
        print("Eso no es un número valido. Intenta de nuevo") # Si la entrada no es un número, damos un mensaje de error
        
print(f"La suma total de los números es: {suma}")
    