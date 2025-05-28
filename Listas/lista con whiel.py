"""Pide al usuario que ingrese números enteros hasta que ingrese un 0.
- Cuántos números positivos ingresó.
- Cuántos negativos.
- Y cuál fue el número mayor de todos los que ingresó (sin contar el 0)."""

enteros = []
ingresados=1
positivos = negativos = 0
nummax = None

#ingresar a la lista
while True:
    ingresados = int(input("Ingrese un número positivo: "))
    if ingresados == 0:
        break
    enteros.append(ingresados)
    
#condicionales
for i in enteros:
    if i>0:
        positivos += 1
    elif i<0:
        negativos += 1

#número mayor
for e in enteros:
    if nummax is None or e > nummax:
        nummax = e

print(f"Los numéros positivos son: {positivos}")
print(f"Los numéros negativos son: {negativos}")
print(f"El número máximo de los ingresados es: {nummax}")

