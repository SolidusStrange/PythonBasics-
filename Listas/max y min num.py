"""Pide al usuario 5 números y guarda
los valores en una lista. Luego imprime el mayor y el menor número de la lista."""

lista = []

# Pedimos el primer número por separado
valor = int(input(f"Ingresa un num (1/5): "))
lista.append(valor)
max_num = min_num = valor  # inicializamos ambos con el primer valor

# Los siguientes 4
for num in range(4):
    valor = int(input(f"Ingresa un num ({num+2}/5): "))
    lista.append(valor)

# Buscamos el mínimo y máximo
for i in lista:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i

print(f"\nNúmeros ingresados: {lista}")
print(f"El número máximo es: {max_num}")
print(f"El número mínimo es: {min_num}")