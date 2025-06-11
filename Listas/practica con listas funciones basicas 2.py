"""practicar funciones de listas como append,
 pop, remove, insert, sort, reverse, y hasta una
 opción con list comprehension."""

compras = []

while True:
    print("\n--- Menú de Lista de Compras ---")
    print("1. Agregar artículo")
    print("2. Eliminar artículo por nombre")
    print("3. Eliminar último artículo agregado")
    print("4. Mostrar lista de compras")
    print("5. Ordenar lista alfabéticamente")
    print("6. Ver lista en orden inverso")
    print("7. Mostrar artículos que contienen más de 5 letras (List Comprehension)")
    print("8. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número.")
        continue

    if opcion == 1:
        articulo = input("Ingrese un nuevo articulo a la lista de compras: ")
        if articulo:
            compras.append(articulo)
            print(f"{articulo} fue agregado.")
        else:
            print("No puede ingresar un articulo vacio a la lista")

    elif opcion == 2:
        articulo = input("Ingrese el nombre exacto del artículo a eliminar: ")
        if articulo in compras:
            compras.remove(articulo)
            print(f"'{articulo}' fue eliminado")
        else:
            print(f"'{articulo}' no está en la lista")

    elif opcion ==3:
        if compras:
            eliminado = compras.pop()
            print(f"Se eliminó el último articulo de la lista '{eliminado}'")
        else:
            print("La lista está vacia")

    elif opcion==4:
        if not compras:
            print("Tu lista de compras está vacia. ")
        else:
            print("--- Lista de Compras ---")
            for i, compra in enumerate(compras, 1):
                print(f"{i}. {compra}")

    elif opcion==5:
        if not compras:
            print("No hay lista que ordenar")
        else:
            compras.sort()
            print("La lista ha sido ordenada alfabéticamente")

    elif opcion==6:
        if not compras:
            print("No hay lista que invertir")
        else:
            print("Lista en orden inverso: ")
            for item in reversed(compras):
                print(f"- {item}")

    elif opcion ==7:
        largos = [item for item in compras if len(item) > 5]
        #lo mismo que:
        #largos = []
        #for item in compras:
        #   if len(item)>5:
        #        largos.append(item)
        print("Articulos con más de 5 letras: ")
        print(largos if largos else "Ninguno")

    elif opcion == 8:
        print("Saliendo de la lista de compras.")
        break

    else:
        print("Ingrese una opción válida.")

