edades = [18,5,13,55,35,20,10,5,25]
suma = menor_edad = mayor_edad = 0

#indicar cuantos mayores y menores de edad hoy
#indicar el promedio de edad
#indicar la edad minima y maxima

for edad in edades:
    suma += edad
    #18 menos y mas
    if edad<18:
        menor_edad += 1
    else:
        mayor_edad += 1


#promedio edad    
promedio = suma/len(edades)

print(f"Los de menores edad son: {menor_edad} ")
print(f"Los de menores edad son: {mayor_edad} ")
print(f"El promedio de edades es: {promedio}")

