#mostrar todos los números del 1 al 100, pero si el número es múltiplo de 3 mostrar "Fizz",
#Si es múltiplo de 5 mostrar "Buzz", y si es múltiplo de ambos mostrar "FizzBuzz".

def bucle_for():
    for i in range(1, 101):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

#¿Qué hace continue acá? Si encuentra un múltiplo de 3, 5 o ambos, imprime 
#el texto correspondiente, suma 1 a i y salta al siguiente ciclo. 
def bucle_while_continue():
    i=1
    while i <= 100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            i += 1
            continue
        elif i % 3 == 0:
            print("Fizz")
            i += 1
            continue
        elif i % 5 == 0:
            print("Buzz")
            i += 1
            continue
        print(i)
        i += 1
        
# Menú para elegir versión
print("Elige versión:")
print("1. Bucle for")
print("2. Bucle while")
opcion = input("Ingresa 1 o 2: ")

if opcion == "1":
    bucle_for()
elif opcion == "2":
    bucle_while_continue()
else:
    print("Opción no válida.")
        
