#Contar cuántos múltiplos de 3 hay en una lista

lista = [1, 2, 5, 4, 9, 11, 16, 17, 19, 21]

contador = 0
for num in lista:
    if num%3==0:
        contador += 1
        
print(f"La cantidad de números múltiplos de 3 en la lista es: {contador}")