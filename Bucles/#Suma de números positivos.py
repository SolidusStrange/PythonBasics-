#Suma de números positivos

#Inicializa la variable de suma
acum=0

#bucle comienzo con true y para si detecta un valor negativo
while True:
    num = int(input("Ingrese un numero entero"))
    if num<0:
        break
    acum += num #se genera la variable que acumula y va sumando
print(acum) 
    
    