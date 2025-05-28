import random

inferior = int(input("Ingrese el primer numero: "))
superior = int(input("Ingrese el segundo numero: "))

if inferior<superior:
    num_aleatorio = random.randint(inferior,superior)
    num_ajustado = round(num_aleatorio/4)*4
    if num_ajustado == 0:
        num_ajustado = 1

    num_ingresado = int(input(f"Primer intento. Ingrese un numero entre {inferior} y {superior} "))#3
    if num_ingresado == num_ajustado:
        print("Felicitaciones, adivinaste en el primer intento.")
    else:
        if num_ingresado<num_ajustado:
            print("El numero ingresado es menor")
        else:
            print("El número ingresado es mayor")
            
        num_ingresado = int(input(f"Segundo intento. Ingrese un numero entre {inferior} y {superior} ")) #4
        if num_ingresado == num_ajustado:
            print("Felicitaciones, adivinaste en el segundo intento.")          
        else:
            if num_ingresado<num_ajustado:
                print("El numero ingresado es menor")
            else:
                print("El número ingresado es mayor")
                    
            num_ingresado = int(input(f"Tercer intento. Ingrese un numero entre {inferior} y {superior} "))  
            if num_ingresado == num_ajustado:    
                print("Felicitaciones, adivinaste en el tercer intento.")          
            else:
                print(f"Perdiste, el numero era {num_ajustado}")
                        
else:
    print("Ingrese un rango correcto")
    