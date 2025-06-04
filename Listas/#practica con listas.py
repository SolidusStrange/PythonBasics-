#practica con listas
#mostrar elementos y sus posiciones
#usando indices

frutas = ['manzana', 'banana', 'kiwi', 'pera']

for i in range(len(frutas)):
    print(f"Fruta en posición {i}: {frutas[i]}")
    
print("-----------------------------------------")

for i, fruta in enumerate(frutas):
    print(f"Fruta en posición {i}: {fruta}")
    
print("-----------------------------------------")

#🔹 Ejercicio 2: Contar cuántos elementos hay que empiezan con la letra "p"
frutas = ['pera', 'manzana', 'plátano', 'kiwi', 'papaya']
contador = 0

for fruta in frutas:
    if fruta.startswith("p"):
        contador += 1

print("La cantidad de frutas que empiezan con P: ",contador)

print("-----------------------------------------")
#🔹 Ejercicio 3: Reemplazar los elementos que tengan más de 5 letras con "LARGA"
#👉 Usando índices (porque hay que modificar la lista)

frutas = ['pera', 'manzana', 'plátano', 'kiwi', 'papaya']

for i in range(len(frutas)):
    if len(frutas[i])>5:
        frutas[i] = "larga"
        
print(frutas)        

#Ejercicio 4: Imprimir una lista al revés usando índices

numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])
    
    
