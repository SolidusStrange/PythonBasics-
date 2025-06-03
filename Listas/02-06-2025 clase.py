opcion = 0
estudiantes = []

while True:
    print("---------------------")
    print("1. Agregar Estudiante")
    print("2. Listar Estudiantes")
    print("3. Eliminar Estudiante")
    print("4. Modificar Estudiantes")
    print("5. Salir")
    print("---------------------")

    try:
        opcion= int(input("Ingrese opción"))
    except ValueError:
        print("Ingrese un valor númerico")

    if opcion==1:
        estudiante = input("Ingrese nombre del estudiante")
        estudiantes.append(estudiante)
        print("Usted ingresado")
    
    elif opcion==2:
        print("La lista de estudiantes es: ")
        for i in estudiantes:
            print(i)

    elif opcion==3:
        delete = input(("Qué estudiante desea eliminar de la lista?"))
        estudiantes.remove(delete) #revisar opcion 3

    elif opcion == 4:
        modificar = input("¿Qué estudiante desea modificar? ")
        if modificar in estudiantes:
            nuevo_nombre = input("¿Por cuál otro estudiante desea reemplazarlo? ")
            estudiantes[estudiantes.index(modificar)] = nuevo_nombre
            print("Estudiante reemplazado")
        else:
            print("El estudiante no se encuentra en la lista.")

    elif opcion==5:
        print("Saliendo del programa...")
        break

    else:
        print("Ingrese una opción válida")
