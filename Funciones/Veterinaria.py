import funcionesVeterinaria

opcion = 0

while opcion != 8:
    print("Veterinaria Cucho")
    print("1. Agregar Mascota")
    print("2. Listar Mascotas")
    print("3. Eliminar Mascotas")
    print("4. Buscar Mascotas")
    print("5. Agendar hora")
    print("6. Listar horas agendadas")
    print("7. Ver horas disponibles")
    print("8. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea"))
    except ValueError:
        print("Ingrese la opcion correcta")

    if opcion == 1:
        funcionesVeterinaria.agregarAnimal()
    elif opcion == 2:
        funcionesVeterinaria.listarAnimales()
    elif opcion == 3:
        funcionesVeterinaria.eliminarMascota()
    elif opcion == 4:
        funcionesVeterinaria.buscarMascota()
    elif opcion == 5:
        funcionesVeterinaria.agendarHora()
    elif opcion == 6:
        funcionesVeterinaria.listarHoras()
    elif opcion == 7:
        funcionesVeterinaria.verHorasDisponibles()
    elif opcion == 8:
        print("Salir")
    else:
        print("Ingrese una opción válida")