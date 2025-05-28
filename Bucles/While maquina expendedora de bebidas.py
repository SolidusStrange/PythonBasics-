opcion = 1
precioAgua = 800
precioGaseosa = 1500
precioJugo = 1800
precioEnergetica = 2500 
precioCafe = 1200
cantAgua = cantGaseosa = cantJugo = cantEnergetica = cantCafe = 10
compra = vuelto = 0

while opcion != 2:
    # menú
    try:
        opcion = int(input("Ingrese la opción que desea:\n1. Ver el menú de bebidas\n2. Salir del programa\n"))
    except ValueError:
        print("Ingrese un valor numérico.")
        continue

    if opcion == 1:
        print(f"---Menú de bebidas---")
        print(f"1. Agua - ${precioAgua} - Stock: {cantAgua}")
        print(f"2. Gaseosa - ${precioGaseosa} - Stock: {cantGaseosa}")
        print(f"3. Jugo Natural - ${precioJugo} - Stock: {cantJugo}")
        print(f"4. Energética - ${precioEnergetica} - Stock: {cantEnergetica}")
        print(f"5. Café en lata - ${precioCafe} - Stock: {cantCafe}")
        
        try:
            compra = int(input("¿Qué opción desea elegir?\n"))
        except ValueError:
            print("Ingrese un valor numérico.")
            continue

        if compra < 1 or compra > 5:
            print("Opción inválida.")
            continue

        while True:
            try:
                dinero = int(input("Ingrese el dinero:\n"))
            except ValueError:
                print("Ingrese un valor numérico.")
                continue

            if compra == 1:
                if cantAgua > 0 and dinero >= precioAgua:
                    cantAgua -= 1
                    vuelto = dinero - precioAgua
                    print(f"Tome su producto. Su vuelto es de ${vuelto}")
                    break
                elif dinero < precioAgua:
                    print("El dinero ingresado no alcanza para la opción elegida.")
                else:
                    print("No hay stock del producto.")
            
            elif compra == 2:
                if cantGaseosa > 0 and dinero >= precioGaseosa:
                    cantGaseosa -= 1
                    vuelto = dinero - precioGaseosa
                    print(f"Tome su producto. Su vuelto es de ${vuelto}")
                    break
                elif dinero < precioGaseosa:
                    print("El dinero ingresado no alcanza para la opción elegida.")
                else:
                    print("No hay stock del producto.")

            elif compra == 3:
                if cantJugo > 0 and dinero >= precioJugo:
                    cantJugo -= 1
                    vuelto = dinero - precioJugo
                    print(f"Tome su producto. Su vuelto es de ${vuelto}")
                    break
                elif dinero < precioJugo:
                    print("El dinero ingresado no alcanza para la opción elegida.")
                else:
                    print("No hay stock del producto.")
            
            elif compra == 4:
                if cantEnergetica > 0 and dinero >= precioEnergetica:
                    cantEnergetica -= 1
                    vuelto = dinero - precioEnergetica
                    print(f"Tome su producto. Su vuelto es de ${vuelto}")
                    break
                elif dinero < precioEnergetica:
                    print("El dinero ingresado no alcanza para la opción elegida.")
                else:
                    print("No hay stock del producto.")
            
            elif compra == 5:
                if cantCafe > 0 and dinero >= precioCafe:
                    cantCafe -= 1
                    vuelto = dinero - precioCafe
                    print(f"Tome su producto. Su vuelto es de ${vuelto}")
                    break
                elif dinero < precioCafe:
                    print("El dinero ingresado no alcanza para la opción elegida.")
                else:
                    print("No hay stock del producto.")

            
        
