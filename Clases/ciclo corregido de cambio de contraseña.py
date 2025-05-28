pwd = "gatito"
passIngreso = ""
redFlag = True
estado = 0
intentos = 0
pregunta_secreta = "perro"
respuesta = ""


while redFlag: #bandera que inicializa el bucle
    passIngreso = input("Ingrese contraseña: ")

#si la password es ingresada es igual a gatito
    if passIngreso == pwd:
        estado = 1 
        break  # salir del ciclo si ingresó bien

#verificar la cantidad de intentos
    elif intentos == 2:
        estado = 2
        respuesta = ""  # reiniciar la respuesta

        while respuesta not in ("si", "no"): #similar a respuesta !="si" o respuesta !="no"
            respuesta = input("¿Desea desbloquear la cuenta? (si/no): ").lower()
            if respuesta == "si":
                animal = input("¿Cuál es su animal favorito?: ").lower()
                if animal == pregunta_secreta:
                    print("Desbloqueo exitoso. Ingrese nueva contraseña.")
                    pwd = input("Nueva contraseña: ")
                    intentos = 0
                    redFlag = True
                else:
                    print("Respuesta incorrecta. Cuenta bloqueada.")
                    redFlag = False
            elif respuesta == "no":
                print("Cuenta bloqueada.")
                redFlag = False
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos}/3")

# Mensaje final
if estado == 1:
    print("¡Ingreso correcto!")
elif estado == 2:
    print("Cuenta bloqueada.")

