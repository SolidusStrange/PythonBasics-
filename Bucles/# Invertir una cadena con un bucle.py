# Invertir una cadena con un bucle
#Pide al usuario una palabra o frase, y luego usa
#un bucle para imprimirla al revés, carácter por carácter.

texto = input("Ingrese una palabra o frase")

longitud = len(texto)

for i in range(longitud -1, -1, -1): #si fuese n=5, 4, 3, 2, 1, 0
    print(texto[i], end="") #end="" evita el salto de linea
    
print() #para dejar una linea al final