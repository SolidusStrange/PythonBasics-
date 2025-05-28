numero = input("Ingresa un número entero positivo: ")
suma_digitos = 0

for digito in numero:
    suma_digitos += int(digito)
    
print(f"La suma de los dígitos es: {suma_digitos}")