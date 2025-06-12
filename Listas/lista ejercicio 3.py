"""append, remove, insert, pop, count, index, clear, y también in y not in."""


libros = []

while True:
    print("\n--- Menú de Biblioteca ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Insertar libro en una posición específica")
    print("4. Buscar un libro")
    print("5. Contar cuántas veces aparece un libro")
    print("6. Mostrar todos los libros")
    print("7. Borrar todos los libros")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion==1:
        libro = input("Ingrese el libro que desea agregar: ")
        libros.append(libro)
        print(f" '{libro}' fue añadido al inventario.")

    elif opcion==2:
        libro = input("Ingrese el libro a eliminar")
        if libro in libros:
            libros.remove(libro)
            print(f"'{libro}' fue eliminado.")
        else:
            print(f"'{libro}' no se encuentra en la biblioteca.")

    elif opcion ==3:
        libro = input("Nombre del libro a insertar: ")
        try:
            indice = int(input("En qué posición desea ingresar el libro (0 para el inicio)"))
            libros.insert(indice, libro)
            print(f"{libro} fue insertado en la posición {indice}.")
        except (ValueError, IndexError):
            print("Posición no válida")

    elif opcion ==4:
        libro = input("Ingrese el nombre del libro a buscar: ")
        if libro in libros:
            posicion = libros.index(libro)
            print(f"'{libro}' se encuentra en la posición")
        else:
            print(f"'{libro}' no se encuentra en la lista")

    elif opcion ==5:
        libro = input("Ingrese el nombre del libro que desea contar: ")
        cantidad = libros.count(libro)
        print(f"Hay {cantidad} del libro: '{libro}' ")

    elif opcion ==6:
        if not libros:
            print("No hay libros registrados.")
        else:
             print("Lista de libros: ")
            for i, book in enumerate(libros, 1):
                print(f"{i}. {book}")

    elif opcion ==7:
        confirmacion = input("¿Estás seguro de que quieres borrar todos los libros? (s/n)")
        if confirmacion.lower() == "s":
            libros.clear()
            print("Inventario eliminado")
        else:
            print("Operación cancelada.")
    elif opcion ==8:
        print("Saliendo del sistema de biblioteca")
        break

    else:
        print("Ingrese una opción válida. Intente nuevamente")
