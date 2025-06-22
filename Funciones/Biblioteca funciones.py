biblioteca = []

def agregar_libro():
    titulo = input("Ingrese el nombre del libro").strip()
    autor = input("Ingrese el nombre del autor del libro").strip()

    while True:
        try:
            anio = int(input("Ingrese el año de la publicación"))
            if anio<1900:
                print("El año no puede ser menor a 1900")
            else:
                break
        except ValueError:
            print("Ingrese un valor númerico")

    #diccionario
    libros = {"titulo": titulo,
              "autor": autor,
              "anio": anio,
              "estado": "disponible"
                }

    biblioteca.append(libros)
    print(f"Libro {libros['titulo']} agregado con éxito")

def mostrar_libro():
    if not biblioteca:
        print("No hay libros registrados")
    else:
        print("-----Libros en la biblioteca-----")
        for libro in biblioteca:
            print(libro)

def buscar_libro():
    libro_buscado = input("Ingrese el libro a buscar").strip().lower()
    encontrados = []

    for libro in biblioteca:
        if libro_buscado in libro["titulo"].lower() or libro_buscado in libro["titulo"].lower():
            encontrados.append(libro_buscado)

    if encontrados:
        print("----Libros encontrados----")
        for libro in encontrados:
            print(libro)
    else:
        print("No se ha encontrado el libro en la biblioteca")

def prestar_libro():
    titulo = input("Ingrese el título del libro que desea prestar: ").strip().lower()
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo:
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                print("--> Libro prestado con éxito")
                return
            else:
                print("El libro se encuentra prestado")
                return
    print("El libro no está en la biblioteca")

def devolver_libro():
    titulo = input("Ingrese el titulo del libro que desea devolver: ").strip().lower()
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo:
            if libro["estado"] == "prestado":
                libro["estado"] = "disponible"
                print(f"Libro {libro['titulo']} devuelto con éxito")
                return
            else:
                print("El libro ya estaba dispionible")
                return
    print("Libro no encontrado")

def eliminar_libro():
    titulo = input("Ingrese el libro a eliminar")
    encontrado = False

    for libro in biblioteca:
        if libro["titulo"].lower() == titulo:
            encontrado = True
            if libro["estado"] == "disponible":
                biblioteca.remove(libro)
                print(f"El libro {libro['titulo']} fue eliminado con éxito ")
            else:
                print("El libro no está disponible")
        if not encontrado:
            print("El libro a eliminar no está en la biblioteca")


def menu():
    while True:
        print("Menú biblioteca:")
        print("1. Agregar libro")
        print("2. Mostrar libros de la biblioteca")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro de la biblioteca")
        print("7. Salir")

        opcion = input("Seleccionar una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libro()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            eliminar_libro()
        elif opcion == "7":
            print("--> Adiós........")
            break;
        else:
            print("--> Opción no valida, intente nuevamente...")

menu()

