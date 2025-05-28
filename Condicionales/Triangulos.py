lado1 = float(input("Ingrese el lado del triangulo"))
lado2 = float(input("Ingrese el lado del triangulo"))
lado3 = float(input("Ingrese el lado del triangulo"))

#Verifica si los lados forman un triángulo válido.
if ((lado1+lado2)>lado3) and ((lado2+lado3)>lado1) and ((lado3+lado1)>lado2):
    if lado1==lado2==lado3:
        print("El triángulo es equilatero")
    elif (lado1==lado2) or (lado2==lado3) or (lado3==lado1):
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
else:
    print("El triángulo no es válido")