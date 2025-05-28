#Mostrar solo los pares de una lista hasta encontrar el primer impar

lista = [2, 4, 6, 8, 10, 15, 20, 30, 55, 33]

for num in lista:
    if num%2!=0:
        print(f"Parado el bucle en el número impar: {num}")
        break
    print(num)
    
