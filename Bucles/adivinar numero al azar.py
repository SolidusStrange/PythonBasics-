import random

numero_secreto = random.randint(1, 10) #el numero aleatorio generado
intentos = 3 #determinar la cantidad de intentos

print("Adivina el número entre 1 y 10. Tienes 3 intentos.")

#bucle para los intentos
for i in range(intentos):
    intento_usuario = int(input(f"Intento {i+1}: Ingresa tu número: "))#solicitamos el numero

    #comprobamos si es correcto
    if intento_usuario == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    else:
        # Si no es correcto, indicar si es mayor o menor
        if intento_usuario < numero_secreto:
            print("El número es mayor. Intenta nuevamente.")
        else:
            print("El número es menor. Intenta nuevamente.")
            
if intento_usuario != numero_secreto:
    print(f"Lo siento, no adivinaste el número. El número correcto era {numero_secreto}.")




