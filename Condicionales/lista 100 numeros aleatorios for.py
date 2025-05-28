import random
#creamos una lista con 100 numeros aleatorios entre el 1 y el 100
num = [] #creamos una lista vacia, no necesita maximo en python
for i in range(100): #para en 100, pero inicia del 0 y llega hasta el 99
    num.append(random.randint(1, 100)) #random.randint genera un num aletaorio entre el rango, append() agrega un valor al final de una lista
 
#contamos personas de entre 50 y 75   
contador = 0 #definimos la variable contador = 0 
for i in range(100): # Recorre del 0 al 99 (100 elementos)
    if num[i]>=50 and num[i]<=75: #para el numero de la lista i, compararlo con el rango
        contador+=1
print(f"La cantidad de personas en el rango de 50 a 75 años es: {contador}")        
        
#contamos para mayores de 80
contador = 0 #reseteamos contador
for i in range(100):
    if num[i]>80:
        contador+=1
print(f"La cantidad de personas mayores de 80 años son: {contador}") 

#contamos para menores de 30
contador = 0 #reseteamos contador
for i in range(100):
    if num[i]<30:
        contador+=1
print(f"La cantidad de personas menores de 30 años son: {contador}")              
 
#imprimimos los primeros 10 numeros
print("Primeros 10 números generados:", num[:10])                