#ver cuál de los tres es menor
num1 = int(input("Ingrese numero 1"))
num2 = int(input("Ingrese numero 2"))
num3 = int(input("Ingrese numero 3"))

if num1<num2 and num1<num3:
    print(f"El numero menor es: {num1}")
elif num2<num3: 
    print(f"El numero menor es: {num2}")
else:
    print(f"El numero menor es: {num3}")
    
         