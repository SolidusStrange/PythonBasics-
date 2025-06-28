# Lista para guardar las entradas
entradas = []


# Función para comprar una entrada
def comprar_entrada():

    while True:
        nombre = input("Ingrese su nombre: ").lower().strip()
        repetido = False
        for entrada in entradas:
            if entrada["nombre"].lower() == nombre:
                print("El comprador ya está registrado. Intente nuevamente")
                repetido = True
                break

        if not repetido:
            break

    while True:
        tipo = input("Ingrese el tipo de entrada(Ingrese G o V): ").upper()
        if tipo == "G" or tipo == "V":
            break
        else:
            print("Ingrese un tipo de entrada válido.")

    while True:
        clave_confirmacion = input("Ingrese la clave de confirmación: ")

        if len(clave_confirmacion)<6:
            print("La clave debe tener al menos 6 caracteres. Ingrese nuevamente.")
            continue

        contiene_mayuscula = False
        for c in clave_confirmacion:
            if c.isupper():
                contiene_mayuscula = True
                break

        if not contiene_mayuscula:
            print("Debe tener al menos una mayuscula")
            continue

        contiene_numero = False
        for c in clave_confirmacion:
            if c.isdigit():
                contiene_numero = True
                break

        if not contiene_numero:
            print("Debe tener al menos un número")
            continue

        if " " in clave_confirmacion:
            print("No debe tener espacios")
            continue

        break

    comprador = {
        "nombre": nombre,
        "tipo": tipo,
        "clave": clave_confirmacion
        }

    entradas.append(comprador)
    print("La compra ha sido exitosa.")

# Función para consultar un comprador
def consultar_comprador():
    nombre = input("Ingrese el nombre que desea consultar: ").lower().strip()
    encontrado = False
    for entrada in entradas:
        if entrada["nombre"].lower() == nombre:
            print(f"Nombre: {entrada['nombre']}")
            print(f"Tipo: {entrada['tipo']}")
            print(f"Clave: {entrada['clave']}")
            encontrado = True
            break

    if not encontrado:
        print("El comprador no se encuentra.")

# Función para cancelar una compra
def cancelar_compra():
    nombre = input("Ingrese el nombre asociado a la compra para cancelar: ").lower().strip()
    encontrado = False
    for entrada in entradas:
        if entrada["nombre"].lower() == nombre:
            entradas.remove(entrada)
            print("¡Compra cancelada!")
            encontrado = True
            break

    if not encontrado:
        print("No se pudo cancelar la compra.")


# Función principal con el menú
def main():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            consultar_comprador()
        elif opcion == "3":
            cancelar_compra()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")


# Ejecutar el programa
if __name__ == "__main__":
    main()
