baneados = ["tomas", "andrea", "lucas"]
pregunta_secreta = "¿Cuál es tu color favorito?"
respuesta_correcta = "azul"

usuario = input("Ingrese su nombre: ").lower()

if usuario not in baneados:
    print("Acceso concedido. Bienvenido.")
else:
    print("Estás en la lista de usuarios baneados.")
    intentar = input("¿Deseas intentar desbloquear tu acceso? (si/no): ").lower()

    if intentar == "si":
        intentos = 3
        while intentos > 0:
            respuesta = input(f"{pregunta_secreta} (Intentos restantes: {intentos}): ").lower()
            if respuesta == respuesta_correcta:
                baneados.remove(usuario)
                print("¡Respuesta correcta! Ya no estás baneado. Puedes ingresar.")
                break
            else:
                intentos -= 1
                print("Respuesta incorrecta.")
        
        if intentos == 0:
            print("Has agotado tus intentos. Acceso denegado.")
    else:
        print("Acceso denegado.")