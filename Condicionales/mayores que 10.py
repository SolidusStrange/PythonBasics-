n = int(input("Ingrese cuantos números quiere ingresar"))
contador = 0
for i in range(n):
    num = int(input("Ingrese numero entero"))
    if num>10:
        contador += 1
        
print(f"La cantidad de numeros mayores que 10 es: {contador}")
        