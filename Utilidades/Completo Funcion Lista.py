from datetime import date, datetime 

from Python.lista import contrasena

libros = [
    {
        "nombre": "cien años de soledad",
        "autor": "gabriel garcia marquez",
        "fecha_publicacion": date(1967, 5, 30),
        "genero": "realismo mágico",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "1984",
        "autor": "george orwell",
        "fecha_publicacion": date(1949, 6, 8),
        "genero": "distopía",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "el principito",
        "autor": "antoine de saint-exupery",
        "fecha_publicacion": date(1943, 4, 6),
        "genero": "cuento filosófico",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "la sombra del viento",
        "autor": "carlos ruiz zafón",
        "fecha_publicacion": date(2001, 4, 12),
        "genero": "novela",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "don quijote de la mancha",
        "autor": "miguel de cervantes",
        "fecha_publicacion": date(1605, 1, 16),
        "genero": "clásico",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "rayuela",
        "autor": "julio cortázar",
        "fecha_publicacion": date(1963, 6, 28),
        "genero": "novela experimental",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "el alquimista",
        "autor": "paulo coelho",
        "fecha_publicacion": date(1988, 1, 1),
        "genero": "ficción",
        "estado": "disponible",
        "dueño": None
    },
    {
        "nombre": "farenheit 451",
        "autor": "ray bradbury",
        "fecha_publicacion": date(1953, 10, 19),
        "genero": "ciencia ficción",
        "estado": "disponible",
        "dueño": None
    }
]
prestados = []
usuarios = []
usuario_actual = None

def registrar_usuario():
    while True:
        correo = input("Ingrese su correo electrónico (example@gmail.com)")
        #VALIDAR QUE TENGA UN @
        if not "@" in correo:
            print("El correo debe llevar un @. Intente nuevamente.")
            continue
        #VALIDAR QUE TENGA UN .
        if correo.endswith(".com") or correo.endswith(".cl"):
            break
        else:
            print("Debe terminar con (.com o .cl)")
            continue

    while True:
        contrasena = input("Ingrese su contraseña.")
        #VALIDAR QUE TENGA MÍNIMO 8 CARACTERES
        if len(contrasena) < 8:
            print("Debe tener al menos 8 caracteres. Pruebe nuevamente.")
            continue

        #VALIDAR QUE TENGA AL MENOS UNA LETRA
        contiene_letra = False
        for c in contrasena:
            if c.isalpha():
                contiene_letra = True
                break

        if not contiene_letra:
            print("Debe contener al menos una letra. Intente nuevamente.")
            continue

        #VALIDAR QUE TENGA AL MENOS UN NUMERO
        contiene_numero = False
        for c in contrasena:
            if c.isdigit():
                contiene_numero = True
                break

        if not contiene_numero:
            print("Debe contener al menos un número. Intente nuevamente.")
            continue

        #VALIDAR QUE NO TENGA ESPACIOS
        if " " in contrasena:
            print("No debe contener espacios. Intente nuevamente.")
            continue

        #VALIDAR QUE TENGA AL MENOS UN CARACTER ESPECIAL
        contiene_especial = False
        for c in contrasena:
            if not c.isalnum():
                contiene_especial = True
                break

        if not contiene_especial:
            print("Debe contener al menos un carácter especial. Intente nuevamente.")
            continue

        #agregar diccionario a la lista usuarios
        ficha = {
            "correo": correo,
            "contrasena": contrasena,
            "libros_prestados": []
        }
        usuarios.append(ficha)
        print("Usuario registrado con éxito.")

        break  #una vez se cumpla todo se rompe el break

def iniciar_sesion():
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su correo electrónico: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()

        # Buscar usuario por correo
        for ingreso in usuarios:
            if ingreso["correo"] == usuario:
                if ingreso["contrasena"] == contrasena:
                    print("Usuario ingresado correctamente.")
                    return ingreso  # Éxito: salir de la función
                else:
                    print("Contraseña incorrecta. Intente nuevamente.")
                    intentos += 1
                    break
        else:
            # Si no entra al if dentro del for: usuario no encontrado
            print("Correo no registrado. Intente nuevamente.")
            intentos += 1

    print("Sin intentos disponibles.")


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
        "estado": "disponible",
        "dueño": None
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


def prestar_libro(usuario_actual):

    titulo = input("Ingrese el nombre título del libro que desea pedir prestado").lower()
    encontrado = False
    for libro in libros:
        if titulo == libro["nombre"].lower():
            encontrado = True
            if libro["estado"] == "disponible" and libro not in prestados:
                print(f"{usuario_actual['correo']} ha prestado el libro '{libro['nombre'].capitalize()}'.")
                prestados.append(libro)
                libro["estado"] = "prestado"
                libro["dueño"] = usuario_actual["correo"]
                usuario_actual["libros_prestados"].append(libro)
                break
            else:
                print("El libro se encuentra prestado.")
                break

    if not encontrado:
        print("El libro no se encuentra en la biblioteca. Revise si el título es el correcto")

def devolver_libro(usuario_actual):
    titulo = input("Ingrese el libro a devolver: ").lower()
    encontrado = False
    for libro in libros:
        if libro["nombre"].lower() == titulo:
            encontrado = True
            if libro["dueño"] == usuario_actual["correo"]:
                libro["estado"] = "disponible"
                libro["dueño"] = None #LIMPIAR EL DUEÑO CADA VEZ QUE DEVUELVA
                prestados.remove(libro)
                usuario_actual["libros_prestados"].remove(libro)
                print("Libro devuelto exitosamente.")
                break
            else:
                print("Libro no lo tiene el usuario actual.")
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

def mostrar_prestados():
    if not usuario_actual:
        print("Debe iniciar sesión primero.")
        return

    if not usuario_actual["libros_prestados"]:
        print("No tienes libros prestados actualmente.")
        return

    print("Libros que has prestado:")
    for i, libro in enumerate(usuario_actual["libros_prestados"],1):
        print(f"{i}. {libro['nombre'].capitalize()} - {libro['autor'].capitalize()} ({libro['fecha_publicacion']}) - {libro['genero'].capitalize()}")

# Menú principal
while True:
    print("\nBiblioteca Comunitaria")

    if usuario_actual:
        print(f"Sesión activa: {usuario_actual['correo']}")
        print("1. Agregar libro")
        print("2. Listar libros disponibles")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro por título")
        print("6. Eliminar libro")
        print("7. Mostrar libros prestados")
        print("8. Cerrar sesión")
        print("9. Salir")
    else:
        print("1. Registro de usuario")
        print("2. Inicio de sesión")
        print("3. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    if usuario_actual:
        if opcion == 1:
            agregar_libro()
        elif opcion == 2:
            listar_libros()
        elif opcion == 3:
            prestar_libro(usuario_actual)
        elif opcion == 4:
            devolver_libro(usuario_actual)
        elif opcion == 5:
            buscar_libro()
        elif opcion == 6:
            eliminar_libro()
        elif opcion == 7:
            mostrar_prestados(usuario_actual)
        elif opcion == 8:
            print(f"Sesión cerrada para {usuario_actual['correo']}.")
            usuario_actual = None
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
    else:
        if opcion == 1:
            registrar_usuario()
        elif opcion == 2:
            usuario_actual = iniciar_sesion()
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")
