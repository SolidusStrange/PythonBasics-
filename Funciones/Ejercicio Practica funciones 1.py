from datetime import datetime

libros = []
prestados = []

def agregar_libro():
    nombre = input("Ingrese el nombre del libro que desea añadir: ").lower().strip()

    while True:
        autor = input("Ingrese el nombre del autor: ").lower().strip()
        if all(c.isalpha() or c == " " for c in autor) and autor:
            break
        else:
            print("Sólo puede usar letras y espacios. Ingrese nuevamente.")

    while True:
        publicacion = input("Ingrese la fecha en formato dd/mm/yyyy: ")
        try:
            fecha = datetime.strptime(publicacion, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Use dd/mm/yyyy.")

    genero = input("Ingrese el genero del libro a añadir: ").lower()

    libro = {
        "nombre": nombre,
        "autor": autor,
        "fecha_publicacion": fecha.date(),
        "genero": genero,
        "estado": "disponible"
        }

    libros.append(libro)
    print("Libro agregado correctamente.")

def listar_libros():
    print("----BIBLIOTECA----")
    encontrados = [libro for libro in libros if libro["estado"] == "disponible"]

    if not encontrados:
        print("No hay libros disponibles en la biblioteca.")
    else:
        for i, libro in enumerate(encontrados, 1):
            print(f"{i}. {libro['nombre'].capitalize()} - {libro['autor'].capitalize()} ({libro['fecha_publicacion']}) - {libro['genero'].capitalize()}")


def prestar_libro():
    titulo = input("Ingrese el nombre título del libro que desea pedir prestado").lower()
    encontrado = False
    for libro in libros:
        if titulo == libro["nombre"].lower():
            encontrado = True
            if libro["estado"] == "disponible":
                print("Libro prestado con éxito.")
                prestados.append(libro)
                libro["estado"] = "prestado"
                break
            else:
                print("El libro se encuentra prestado.")
                break

    if not encontrado:
        print("El libro no se encuentra en la biblioteca. Revise si el título es el correcto")

def devolver_libro():
    titulo = input("Ingrese el libro a devolver: ").lower()
    encontrado = False
    for libro in libros:
        if libro["nombre"].lower() == titulo:
            encontrado = True
            libro["estado"] = "disponible"
            prestados.remove(libro)
            print("Libro devuelto exitosamente.")
            break

    if not encontrado:
        print("El libro a devolver no se encuentra en la biblioteca. Revise el título ingresado")

def buscar_libro():
    titulo = input("Ingrese el libro que busca: ").lower()
    encontrado = False
    for libro in libros:
        if libro["nombre"].lower() == titulo:
            encontrado = True
            print(f"Nombre: {libro['nombre'].capitalize()}")
            print(f"Autor: {libro['autor'].capitalize()}")
            print(f"Fecha de Publicación: {libro['fecha_publicacion']}")
            print(f"Genero: {libro['genero'].capitalize()}")
            print(f"Estado: {libro['estado'].capitalize()}")
            break

    if not encontrado:
        print("El libro consultado no se encuentra en la biblioteca.")

def eliminar_libro():
    titulo = input("Ingrese el libro a eliminar: ").lower()
    encontrado = False

    for libro in libros:
        if titulo == libro["nombre"].lower():
            encontrado = True
            libros.remove(libro)
            if libro in prestados:
                prestados.remove(libro)
            print("Libro eliminado")
            break

    if not encontrado:
        print("El libro a eliminar no se encuentra en la biblioteca")

# Menú principal
opcion = 0
while opcion != 7:
    print("\nBiblioteca Comunitaria")
    print("1. Agregar libro")
    print("2. Listar libros disponibles")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por título")
    print("6. Eliminar libro")
    print("7. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        listar_libros()
    elif opcion == 3:
        prestar_libro()
    elif opcion == 4:
        devolver_libro()
    elif opcion == 5:
        buscar_libro()
    elif opcion == 6:
        eliminar_libro()
    elif opcion == 7:
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")
