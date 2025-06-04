#🔸 Ejercicio 1: Reemplazar con "CORTA"
#Dada una lista de palabras, reemplaza todas las que tienen 4 letras o menos por la palabra "CORTA".

palabras = ['luz', 'camino', 'sol', 'aventura', 'paz']

for i in range(len(palabras)):
    if len(palabras[i])<=4:
        palabras[i] = "corta"
    
print(palabras)

#🔸Ejercicio 2: Contar cuántos números son múltiplos de 3

numeros = [3, 5, 9, 12, 14, 18, 21, 25, 30]
# Resultado esperado: 6

contador = 0
        
for i in numeros:
    if i%3==0:
        contador+=1

print(contador)


#🔸Ejercicio 3: Mostrar índice y valor de los elementos mayores a 50

valores = [10, 55, 70, 40, 90]
# Resultado esperado:
# Índice 1: 55
# Índice 2: 70
# Índice 4: 90

for i in range(len(valores)):
    if valores[i]>50:
        print(f"Indice {i}: {valores[i]}")
        
#🔸 Ejercicio 4: Crear una nueva lista con los elementos que no contengan la letra 'a'

palabras = ['sol', 'luna', 'estrella', 'nube', 'cielo']
# Resultado esperado: ['sol', 'nube', 'cielo']

for caracter in palabras:
    if "a" not in caracter:
        print(caracter)

#🔸Ejercicio 5: Invertir el orden de una lista usando un bucle

original = [1, 2, 3, 4, 5]
# Resultado esperado: [5, 4, 3, 2, 1]

for i in range(len(original),0,-1):
    print(i)