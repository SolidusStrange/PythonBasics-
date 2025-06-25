# Funciones
def comprar_entrada():
    # Aquí irá la lógica para registrar un comprador
    pass

def consultar_comprador():
    # Aquí irá la lógica para consultar datos de un comprador
    pass

def cancelar_compra():
    # Aquí irá la lógica para cancelar una compra
    pass

def mostrar_menu():
    print("MENU PRINCIPAL")
    print("1.- Comprar entrada.")
    print("2.- Consultar comprador.")
    print("3.- Cancelar compra.")
    print("4.- Salir.")

# Función principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

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
