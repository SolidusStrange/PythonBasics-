# Número primo
contador = primos = no_primos = 0

# Validar cantidad de números
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de números a verificar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero.")

# Repetir por la cantidad ingresada
while contador < cantidad:
    # Validar número entero
    try:
        numero = int(input("Ingrese número: "))
    except ValueError:
        print("Debe ingresar un número entero.")
        continue  # volver a pedir este número

    es_primo = True

    # Verificar si es primo
    if numero >= 2:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
    else:
        es_primo = False

    # Resultados
    if es_primo:
        print("Es primo.")
        primos += 1
    else:
        print("No es primo.")
        no_primos += 1

    contador += 1

# Mostrar resumen
print(f"\nSe ingresaron {primos} números primos.")
print(f"Se ingresaron {no_primos} números no primos.")
