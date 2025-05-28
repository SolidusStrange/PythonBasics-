"""Pide 10 números. Usa una lista para almacenarlos y cuenta cuántos son positivos, 
cuántos negativos y cuántos ceros."""

numeros = []

#ingresar los numeros a la lista
for num in range(1,11):
    num_ingresado = int(input(f"Ingrese un numero {num}/10: "))
    numeros.append(num_ingresado)
    
#condicional de lista
positivos = negativos = ceros = 0
for i in numeros:
    if i>0:
        positivos += 1
    elif i==0:
        ceros += 1
    else:
        negativos += 1

print(f"La cantidad de positivos son: {positivos}/10\nLa cantidad de ceros son: {ceros}/10\nLa cantidad de negativos son: {negativos}/10")