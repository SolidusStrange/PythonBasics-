"""Pide al usuario que ingrese las edades de 10 personas. Guarda todas las edades en una lista. Luego, indica:
Cuántas personas son menores de edad (menos de 18 años).
Cuántas son adultas (entre 18 y 60).
Cuántas son adultos mayores (más de 60 años)."""

edades = []
menores = mayores = adultos = edad = 0
maxEdad = 0
minEdad = 100

#ingresar a lista

for num in range(10):
    while True: 
        edad = int(input(f"Ingrese la edad de la persona {num+1}/10: "))
        if edad<0:
            print("La edad no puede ser negativa. Intente nuevamente.")
        else:
            edades.append(edad)
            break #salir del while si es valida
    
#edadesmaxymin
for maxmin in edades:
    if maxmin<minEdad:
        minEdad = maxmin
    elif maxmin>maxEdad:
        maxEdad = maxmin
    
print(f"El número mínimo es: {minEdad} y el número máximo es: {maxEdad}")
    
#condicionales
for edad in edades:
    if edad<18:
        menores +=1
    elif edad<=60:
        adultos +=1
    else:
        mayores +=1

total = menores + adultos + mayores

promedioMenores = menores/total
promedioMayores = mayores/total
promedioAdultos = adultos/total

print(f"El promedio de edad de menores es {promedioMenores}\nEl promedio de edad de mayores es {promedioMayores}\nEl promedio de edad de adultos es {promedioAdultos}")

print(f"Las personas menores de edad son: {menores}\nLas personas adultas son: {adultos}\nLas personas adultos mayores son: {mayores}")

"""Validar que no se ingresen edades negativas.
Calcular el promedio por grupo.
Mostrar la edad más alta y la más baja."""

