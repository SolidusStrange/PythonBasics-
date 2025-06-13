nombres = []
notas = []

while True:
    print("\n--- Menú del Sistema de Notas ---")
    print("1. Registrar alumno y nota")
    print("2. Mostrar todos los alumnos y sus notas")
    print("3. Mostrar promedio de notas")
    print("4. Buscar nota por nombre")
    print("5. Eliminar alumno por nombre")
    print("6. Mostrar lista de aprobados (nota >= 60)")
    print("7. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un valor numérico válido.")
        continue

    if opcion == 1:
        nombre = input("Ingrese el nombre del alumno")
        nota = float(input("Ingrese la nota del alumno"))
        nombres.append(nombre)
        notas.append(nota)

    elif opcion == 2:
        print("Lista de alumnos: ")
        for nombre, nota in zip(nombres, notas): #zip une por indice ej nombre 0 le corresponde nota 0
            print(f"Alumno: {nombre} Nota: {nota}")

    elif opcion == 3:
        if not notas:
            print("No hay notas ingresadas")
        else:
            total_notas = sum(notas)
            cantidad = len(notas)
            promedio = total_notas/cantidad
            print(f"El promedio de notas es: {promedio}")

    elif opcion == 4:
        # Aquí buscarás una nota por nombre
        pass

    elif opcion == 5:
        # Aquí eliminarás un alumno por nombre
        pass

    elif opcion == 6:
        # Aquí usarás list comprehension para mostrar los aprobados
        pass

    elif opcion == 7:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
