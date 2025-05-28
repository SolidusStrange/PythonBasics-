#Probando repetir en edades
suma = 0
contador = 0

while True:
    edad = int(input("Ingrese una edad (número negativo para salir): "))
    if edad<0:
        break
    suma += edad
    contador += 1
    
if contador > 0:
    print(f"Cantidad de edad ingresadas: {contador}")
    print(f"Promedio de edades: {suma / contador}") 
else:    
    print("No se ingresaron edades validas")
    