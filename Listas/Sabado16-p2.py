#listaSuper
sw = 1
listaSuper = []
valorSuper = []

print("Presione 1 para ingresar los productos del super")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción "))
if(op == 1):
    while sw==1:
        print("----------------------------------------------------------")
        producto=input("Incorpore su producto, para salir, presione 0: ")
        if producto != "0":
            listaSuper.append(producto)
            valorProducto = int(input(f"Incorpore el valor del {producto}:"))
            valorSuper.append(valorProducto) 
            print("---DETALLE BOLETA---")
            print(f"Los productos comprados son: {listaSuper}")
            print(f"La cantidad de productos comprados es: {len(listaSuper)}")
            print(f"La suma total de los productos es: {sum(valorSuper)}")

        else:
            print("Adiós")
            sw=0

else:
    print("Adiós")

