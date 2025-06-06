maxNum = -1
minNum = 101

while True:
    print("\n*** MENÚ PRINCIPAL ***")
    print("1.- Ingresar número.")
    print("2.- Mostrar mayor.")
    print("3.- Mostrar menor.")
    print("4.- Salir.")
    
    try:
        opcion = int(input("Ingrese la opción que desea: "))
    except ValueError:
        print("Ingrese un valor numérico")
        continue

    if opcion == 1:
        while True:
            try:
                numero = int(input("Ingrese un número entre 0 y 100: "))
                if 0 <= numero <= 100:
                    print("Ingreso exitoso")
                    if numero > maxNum:
                        maxNum = numero
                    if numero < minNum:
                        minNum = numero
                    break
                else:
                    print("Debe ingresar un número entre 0 y 100!!")
            except ValueError:
                print("Debe ingresar un número entero!!")

    elif opcion == 2:
        if maxNum != -1:
            print(f"El número mayor hasta el momento es: {maxNum}")
        else:
            print("No se han ingresado números")

    elif opcion == 3:
        if minNum != 101:
            print(f"El número menor hasta el momento es: {minNum}")
        else:
            print("No se han ingresado números")

    elif opcion == 4:
        print("Fin del programa. Adiós")
        break

    else:
        print("Debe ingresar una opción válida")
