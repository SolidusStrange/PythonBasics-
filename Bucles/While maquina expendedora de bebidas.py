opcion = 1
precioAgua = 800
precioGaseosa = 1500
precioJugo = 1800
precioEnergetica = 2500 
precioCafe = 1200
cantAgua = cantGaseosa = cantJugo = cantEnergetica = cantCafe = cantAgua = 10
compra = 0

while opcion != 2:
    #menu
    opcion = int(input("Ingrese la opción que desea:\n1. Ver el menú de bebidas\n2. Salir del programa"))
    if opcion == 1:
        print(f"---Menu de bebidas---")
        print(f"1. Agua/{precioAgua}/{cantAgua}")
        print(f"2. Gaseosa/{precioGaseosa}/{cantGaseosa}")
        print(f"3. Jugo Natural/{precioJugo}/{cantJugo}")
        print(f"4. Energética/{precioEnergetica}/{cantEnergetica}")
        print(f"5. Café en lata/{precioCafe}/{cantCafe}")
        compra = int(input("¿Qué opción desea elegir?"))
        while compra>0 and compra<=5:
            dinero = int(input("Ingrese el dinero"))
            if compra==1:
                if cantAgua>0 and dinero>=precioAgua: #verificamos que haya stock y tenga el dinero para comprar
                    
                    
     
        else: 
            print("Elija una opción válida")
            
        