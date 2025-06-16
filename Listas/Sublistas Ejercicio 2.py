alumnos = []

while True:
    print("\n--- Menú ---")
    print("1. Registrar alumno y nota")
    print("2. Mostrar todos los alumnos")
    print("3. Buscar alumno por nombre")
    print("4. Mostrar cantidad de aprobados (nota ≥ 6)")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        try:
            cantidad = int(input("Ingrese la cantidad de alumnos que quiere ingresar: "))
        except ValueError:
            print("Ingrese un valor numérico.")
            continue

        for i in range(cantidad):
            print(f"\nAlumno {i+1}")
            nombre = input("Ingrese el nombre del alumno: ")
            try:
                nota = float(input("Ingrese la nota del alumno: "))
            except ValueError:
                print("Nota inválida, debe ser un número.")
                continue  # Salta al siguiente alumno

            alumnos.append([nombre, nota])
            print("Alumno añadido")

        print(f"\nSe han ingresado los {cantidad} alumnos.")

    elif opcion == "2":
        if not alumnos:
            print("\nNo hay alumnos registrados.")
        else:
            print("\nLista de alumnos:")
            for alumno in alumnos:
                print(f"{alumno[0]} - Nota: {alumno[1]}")

    elif opcion == "3":
        buscado = input("Ingrese el nombre del alumno a buscar: ")
        encontrado = False
        for alumno in alumnos:
            if alumno[0].lower() == buscado.lower():
                print(f"{alumno[0]} - Nota: {alumno[1]}")
                encontrado = True
                break
        if not encontrado:
            print("Alumno no encontrado.")

    elif opcion == "4":
        contador_aprobados = 0
        print("\nLista de alumnos aprobados (nota ≥ 6):")
        for alumno in alumnos:
            if alumno[1] >= 6:
                print(f"{alumno[0]} - Nota: {alumno[1]}")
                contador_aprobados += 1
        print(f"Total de aprobados: {contador_aprobados}")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
