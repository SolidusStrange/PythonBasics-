libros = []
prestados = []

def agregar_libro():
    pass

def listar_libros():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def buscar_libro():
    pass

def eliminar_libro():
    pass

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
