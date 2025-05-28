#Mostrar los digitos impares de un numero

numero = input("Ingresa un número entero positivo: ")
impares = 0

for digito in numero:
    valor = int(digito)
    if valor%2!=0:
        print(valor)
        impares += 1
        
print(f"\nCantidad de digitos impares: {impares}")

    

    