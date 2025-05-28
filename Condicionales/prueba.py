print("Calculadora")
#solicitud de números
num1=int(input("Ingrese el primer número"))
num2=int(input("Ingrese el segundo número"))

#operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1*num2

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)

#division dependerá si el denominador es 0
if num2!=0:
    division = num1/num2
    print("La división es: ", division)
else:
    print("El denominador no puede ser\n 0")  

    
    