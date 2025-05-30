saldo = 100000

while True:
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea"))
        if opcion<1 or opcion>4:
            print("Elija una opción del menú")
            continue
    except: 
        print("Elija un valor númerico")
        continue
    
    if opcion==1: #consultar saldo
        print(f"El saldo en su cuenta es: {saldo}")
    
    elif opcion == 2: #retiro
        try:
            retiro = int(input("Ingrese la cantidad a retirar: "))
        except ValueError:
            print("Error: Ingrese un valor numérico.")
            continue

        if retiro <= 0:
            print("La cantidad debe ser mayor que cero.")
        elif saldo >= retiro:
            saldo -= retiro
            print(f"Retiro exitoso de ${retiro}. Saldo restante: ${saldo}")
        else:
            print("Fondos insuficientes.")
            
    elif opcion==3: #depositar dinero
        try:
            deposito = int(input("Ingrese la cantidad que quiere depositar"))
        except:
            print("Elija un valor númerico")
            continue
        
        if deposito>0:
            saldo = saldo + deposito
            print(f"La cantidad depositada es de: {deposito}. Su nuevo saldo es de {saldo}")
        else:
            print("No puede ingresar una cantidad negativa")
            continue
        
    elif opcion==4:
        print("Gracias por usar el cajero.")
        break
    