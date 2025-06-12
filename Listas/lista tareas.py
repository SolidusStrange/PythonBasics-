tareas_pendientes = []
tareas_completadas = []

while True:
    print("\n--- Menú de Tareas ---")
    print("1. Ver tareas pendientes")
    print("2. Añadir nueva tarea")
    print("3. Eliminar una tarea")
    print("4. Marcar tarea como completada")
    print("5. Ver tareas completadas")
    print("6. Ordenar tareas alfabéticamente")
    print("7. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un valor numérico válido.")
        continue

    if opcion == 1:
        if not tareas_pendientes:
            print("No hay tareas pendientes.")
        else:
            print("Las tareas pendientes son:")
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}")

    elif opcion == 2:
        tareas = input("¿Qué tarea desea añadir?")
        tareas_pendientes.append(tareas)
        print("Tarea añadida")

    elif opcion == 3:
        if not tareas_pendientes:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}.")
            try:
                indice = int(input("Ingrese el número de la factura que desea remover"))
                tarea_eliminada = tareas_pendientes.remove(indice-1)
                print(f"Tarea {tarea_eliminada} eliminada")
            except (ValueError, IndexError):
                print("Indice no válido")

    elif opcion == 4:
        if not tareas_completadas:
            print("No hay tareas completadas")
        else:
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}")
            try:
                indice = int(input("Ingrese el número de la tarea"))
                tarea_eliminada = tareas.pendientes.remove(indice-1)
                tareas_completadas.append(tarea_eliminada)
                print("Tarea añadida")
            except (ValueError, IndexError):
                print("Indice no válido")

    elif opcion == 5:
        if not tareas_completadas:
            print("No hay tareas completadas")
        else:
            print("Lista de tareas completadas")
            for i, tarea in enumerate(tareas_completadas, 1):
                print(f"{i}. {tarea}")

    elif opcion ==6:
        if not tareas_pendientes:
            print("No hay tareas pendientes")
        else:
            tareas_pendientes.sort()
            print("Tareas ordenadas")

    elif opcion == 7:
        print("Saliendo del programa")
        break
        
    else:
        print("Ingrese una opción válida")

