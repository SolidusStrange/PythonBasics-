productos = ["pan", "leche", "huevo", "arroz", "leche"]

def mostrar_menu():
    print("\n" + "-" * 30)
    print("       Menú de Productos")
    print("-" * 30)
    print("1. Ver lista de productos")
    print("2. Insertar un producto en una posición específica")
    print("3. Agregar producto al final")
    print("4. Contar cuántas veces aparece un producto")
    print("5. Eliminar una aparición de un producto")
    print("6. Ordenar lista alfabéticamente")
    print("7. Invertir lista")
    print("8. Mostrar la posición de un producto")
    print("9. Salir")

def ver_lista():
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {producto}")

def insertar_producto():
    producto_insertado = input("Ingrese el producto a insertar: ").lower()
    try:
        posicion = int(input("Ingrese la posición en la que desea insertar el producto: "))
        if posicion < 0 or posicion > len(productos):
            print(f"La posición está fuera de rango. Se insertará al final.")
        else:
            productos.insert(posicion, producto_insertado)
            print(f"'{producto_insertado}' insertado en la posición {posicion}")
    except ValueError:
        print("Ingrese un valor numérico.")

def agregar_producto():
    producto_ingresado = input("Ingrese el producto que desea añadir: ").lower()
    productos.append(producto_ingresado)
    print(f"'{producto_ingresado}' ingresado.")

def contar_producto():
    producto_a_contar = input("Ingrese el producto que desea contar en la lista: ")
    if producto_a_contar not in productos:
        print(f"El producto '{producto_a_contar}' no está en la lista.")
    else:
        cantidad_contada = productos.count(producto_a_contar)
        print(f"La cantidad contada de '{producto_a_contar}' es de {cantidad_contada}")

def eliminar_producto():
    producto_eliminado = input("Ingrese el producto que desea eliminar: ")
    if producto_eliminado not in productos:
        print(f"El producto '{producto_eliminado}' no está en la lista.")
    else:
        productos.remove(producto_eliminado)
        print(f"Producto '{producto_eliminado}' eliminado de la lista.")

def ordenar_lista():
    productos.sort()
    print("Lista ordenada de forma alfabética.")

def invertir_lista():
    productos.reverse()
    print("Lista invertida.")

def mostrar_posicion():
    indice = input("Ingrese el producto que desea ubicar su posición en la lista: ")
    if indice not in productos:
        print(f"El producto '{indice}' no está en la lista.")
    else:
        posicion = productos.index(indice)
        print(f"El producto '{indice}' está en la posición {posicion + 1} de la lista")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-9): ")

    if opcion == "1":
        ver_lista()
    elif opcion == "2":
        insertar_producto()
    elif opcion == "3":
        agregar_producto()
    elif opcion == "4":
        contar_producto()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        ordenar_lista()
    elif opcion == "7":
        invertir_lista()
    elif opcion == "8":
        mostrar_posicion()
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")