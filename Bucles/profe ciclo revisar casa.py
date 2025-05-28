#Debe ingresar a un cajero e indicar el dinero a retirar
#El programa debe indicar cuantos billetes de cada numeracion debe entregar
#Tiene 100 billetes de cada numeracion

bil20 = bil10 = bil5 = bil2 = bil1 = 100
cant20 = cant10 = cant5 = cant2 = cant1 = 0
opcion = 1

while opcion!=2:
    #definir saldo de billetes
    saldo = bil20*20000+bil10*10000+bil5*5000+bil2*2000+bil1*1000 
    #menu de selección
    print("----El Cajero Feliz----")
    print("Saldo Cajero: ",saldo)
    print("1-Retirar")
    print("2-Salir")
    print("3-Verificar saldos")
    try:
        opcion= int(input("Seleccione opcion"))
        if opcion==1:    
            #reiniciar contadores
            cant20 = cant10 = cant5 = cant2 = cant1 = 0
            #verificación del valor de retiro
            try:
                retiro = int(input("Cuanto desea retirar?"))
            except ValueError:
                print("Ingrese un monto válido")
                continue
            
            if retiro> saldo: #verificar que quede saldo
                print("El saldo del cajero es insuficiente")
            elif retiro<1000: #verificar que el retiro sea mayor al mínimo
                print("Ingrese un retiro valido")
            else: #una vez se verificaron todas las anteriores
                while retiro>=20000 and bil20>0:
                    bil20 = bil20-1
                    cant20 = cant20+1
                    retiro = retiro - 20000
                while retiro>=10000 and bil10>0:
                    bil10 = bil10-1
                    cant10 = cant10+1
                    retiro = retiro - 10000
                while retiro>=5000 and bil5>0:
                    bil5 = bil5-1
                    cant5 = cant5+1
                    retiro = retiro - 5000
                while retiro>=2000 and bil2>0:
                    bil2 = bil2-1
                    cant2 = cant2+1
                    retiro = retiro - 2000
                while retiro>=1000 and bil1>0:
                    bil1 = bil1-1
                    cant1 = cant1+1
                    retiro = retiro - 1000
                #imprimir cantidades
                print("Retiro las siguientes cantidades")
                print("Billetes de $20.000 ", cant20)
                print("Billetes de $10.000 ", cant10)
                print("Billetes de $5.000 ", cant5)
                print("Billetes de $2.000 ", cant2)
                print("Billetes de $1.000 ", cant1)
        elif opcion==2:
            print("Adios")
        elif opcion==3:
            print("-----Saldos-----")
            print("Billetes de $20.000 ", bil20)
            print("Billetes de $10.000 ", bil10)
            print("Billetes de $5.000 ", bil5)
            print("Billetes de $2.000 ", bil2)
            print("Billetes de $1.000 ", bil1)
            print("Saldo del cajero: ", saldo)
        else:
            print("Seleccione opcion correcta")
            
    except ValueError:
        print("Ingrese un valor númerico")