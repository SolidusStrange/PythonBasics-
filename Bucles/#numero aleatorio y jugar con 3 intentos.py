#El programa debe generar un número aleatorio entre 1 y 10. 

def adivina_con_contador_ascendente():
    print("\nVersión 1: contador ascendente (0 → 3)")
    import random 
    numero_secreto = random.randint(1, 10)
    #Luego debe pedir al usuario que lo adivine.  Si adivina, se muestra un mensaje de éxito y se termina. Si falla, tiene hasta 3 intentos.
    # Si falla los 3, se muestra un mensaje diciendo que se acabaron los intentos.
    intentos = 0 #variable inicializada porque es un contador
    while intentos<3: #bucle que verifica cuando se le acaben los intentos
        intento = int(input("Adivina el número (entre 1 y 10): "))
        if intento == numero_secreto: #si es igual al numero buscado, para el bucle y da el resultado
            print("Correcto! Adivinaste el número.")
            break
        else:
            intentos += 1 #si no es igual, se suma un intento
    
    if intentos == 3: #si se le acaban los intentos, esto ya es fuera del bucle
        print(f"Se acabaron los intentos. El número era: {numero_secreto}")        

def adivina_con_contador_descendente():
    print("\nVersión 2: contador descendente (3 → 0)")
    import random 
    numero_secreto = random.randint(1, 10)
    intentos = 3 
    while intentos>0: 
        intento = int(input("Adivina el número (entre 1 y 10): "))
        if intento == numero_secreto:
            print("Correcto! Adivinaste el número.")
            break
        else:
            intentos -= 1 
    
    if intentos == 0: 
        print(f"Se acabaron los intentos. El número era: {numero_secreto}") 
        
# Menú para elegir versión
print("Selecciona la versión del juego:")
print("1. Contador ascendente (0 → 3)")
print("2. Contador descendente (3 → 0)")
opcion = input("Ingresa 1 o 2: ")

if opcion == "1":
    adivina_con_contador_ascendente()
elif opcion == "2":
    adivina_con_contador_descendente()
else:
    print("Opción no válida.")       
