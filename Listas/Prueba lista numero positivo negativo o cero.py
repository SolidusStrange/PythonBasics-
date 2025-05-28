#numeros positivos y negativos
positivos = negativos = ceros = sumaP = sumaN = 0

lista = []
for i in range(10):
    num = int(input("Ingrese un numero (positivos, negativos o cero)"))
    lista.append(num)

#analisis de la lista
    if num>0:
        positivos+=1
        sumaP += num
    elif num==0:
        ceros +=1
    else:
        negativos +=1
        sumaN += num
        
# Promedios con verificación
if positivos > 0:
    print(f"El promedio de los positivos es: {sumaP / positivos:.2f}")
else:
    print("No se ingresaron números positivos.")

if negativos > 0:
    print(f"El promedio de los negativos es: {sumaN / negativos:.2f}")
else:
    print("No se ingresaron números negativos.")

print(f"Cantidad de ceros: {ceros}")

