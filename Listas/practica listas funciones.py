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

    #revisar tareas pendientes
    if opcion == 1:
        if not tareas_pendientes:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes: ")
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}")

    #añadir una nueva tarea
    elif opcion == 2:
        nueva = input("Ingrese la nueva tarea")
        if nueva:
            tareas_pendientes.append(nueva)
            print("Tarea añadida.")
        else:
            print("La tarea no puede estar vacia.")

    elif opcion == 3:
        if not tareas_pendientes:
            print("No hay tareas para eliminar.")
        else:
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}")
            try:
                indice = int(input("Ingrese el número de la tarea a eliminar: "))
                tarea_eliminada = tareas_pendientes.pop(indice-1)
                print(f"Tarea {tarea_eliminada} eliminada")
            except (ValueError, IndexError):
                print("Indice no válido")

    elif opcion == 4:
        if not tareas_pendientes:
            print("No hay tareas para completas.")
        else:
            for i, tarea in enumerate(tareas_pendientes, 1):
                print(f"{i}. {tarea}")
            try:
                indice = int(input("Ingrese el númera de la tarea que quiere completar: "))
                tarea = tareas_pendientes.pop(indice-1)
                tareas_completadas.append(tarea)
            except (ValueError, IndexError):
                print("Indice no válido")

    elif opcion==5:
        if not tareas_completadas:
            print("Aún no hay tareas completadas")
        else:
            for i, tarea in enumerate(tareas_completadas, 1):
                print(f"{i}. {tarea}")

    elif opcion==6:
        if not tareas_pendientes:
            print("No hay tareas para ordenar")
        else:
            tareas_pendientes.sort()

    elif opcion==7:
        print("Saliendo del gestor de tareas.")
        break

    else:
        print("Ingrese una opción válida")
