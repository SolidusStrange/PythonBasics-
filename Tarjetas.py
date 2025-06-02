tarjetas = [None, None, None]
claves = [None, None, None]

while True:
    print("\n1. Ingresar a la oficina")
    print("2. Registrar nueva tarjeta")
    print("3. Ver tarjetas registradas")
    print("4. Salir")
    
    try: 
        opcion = int(input("Ingrese la opción que desee: "))
    except ValueError:
        print("Ingrese un valor numérico")
        continue
    
    if opcion == 1:
        if tarjetas.count(None) == 3:
            print("No existe ningún usuario registrado. Debe registrar un usuario primero.")
        else:
            name = input("Ingrese su número de tarjeta: ")
            password = input("Ingrese su clave: ")
            encontrado = False
            for e in range(len(tarjetas)):
                if tarjetas[e] == name and claves[e] == password:
                    print("Acceso concedido")
                    encontrado = True
                    break
            if not encontrado:
                print("Usuario o contraseña incorrectos")

    elif opcion == 2:
        if tarjetas.count(None) == 0:
            print("Tarjetas llenas. No se pueden registrar más tarjetas.")  
        else:
            nueva_tarjeta = input("Ingrese su número de tarjeta: ") 
            if nueva_tarjeta in tarjetas:
                print("Esta tarjeta ya está registrada.")
            else: 
                for i in range(len(tarjetas)):
                    if tarjetas[i] is None:
                        tarjetas[i] = nueva_tarjeta
                        claves[i] = input("Ingrese su clave: ")
                        print("Tarjeta registrada")
                        break

    elif opcion == 3:  # Ver tarjetas registradas
        print(f"La cantidad de tarjetas vacías es: {tarjetas.count(None)}")
        for i in range(len(tarjetas)):
            print(f"Tarjeta de identificación número {i + 1}: {tarjetas[i]}")
        
    elif opcion == 4:
        print("Saliendo del programa")
        break
    
    else:
        print("Ingrese una opción válida")