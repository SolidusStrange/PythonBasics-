usuarios = []
contrasenas = []

while True:
    print("\n***Menu Principal***")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea: "))
    except ValueError:
        print("Ingrese un valor numérico")
        continue

    # Añadir usuarios
    if opcion == 1:
        while True:
            nuevo_usuario = input("Ingrese su nombre de usuario (escriba 'salir' para parar): ")
            if nuevo_usuario.lower() == "salir":
                break
            if nuevo_usuario in usuarios:
                print("El usuario ya existe. Intente con otro nombre.")
                continue

            contrasena = input("Ingrese la contraseña del alumno: ")
            if len(contrasena) < 4:
                print("La contraseña debe tener al menos 4 caracteres.")
                continue

            usuarios.append(nuevo_usuario)
            contrasenas.append(contrasena)
        print("Lista de alumnos registrados:", usuarios)

    # Ingreso de usuario
    elif opcion == 2:
        usuario_ingresado = input("Ingrese su usuario: ")
        contrasena_ingresada = input("Ingrese su contraseña: ")
        if usuario_ingresado in usuarios:
            indice = usuarios.index(usuario_ingresado)
            if contrasenas[indice] == contrasena_ingresada:
                print("Ingreso exitoso")
            else:
                print("Contraseña incorrecta. Intente nuevamente")
        else:
            print("Usuario no encontrado. Intente nuevamente")

    elif opcion == 3:
        print("La lista de usuarios es:", usuarios)

    elif opcion == 4:
        print("Saliendo del programa")
        break

    else:
        print("Ingrese una opción válida")
