# Funciones
concierto = []
compras_canceladas = []

def comprar_entrada():
    #VERIFICAR QUE NO ESTÉ REPETIDO EN LA LISTA#
    while True:
        repetido = False
        nombre = input("Ingrese su nombre: ")
        for publico in concierto:
            if publico["nombre"] == nombre:
                print("El comprador ya está registrado.")
                repetido = True
                break

        if not repetido:
            break        
    #VERIFICAR QUE SEA G O V LO INGRESADO
    while True:
        entrada = input("Tipo de entrada (G para General / V para VIP): ").upper()
        if entrada == "G" or entrada == "V":
            break
        else:
            print("Tipo inválido. Ingrese V o G.")

    #VERIFICAR QUE EL CODIGO DE CONFIRMACIÓN CUMPLA CON TODAS LAS CONDICIONES
    while True:
        codigo_confirmacion = input("Ingrese el código de confirmación")

        #VERIFICAR CANTIDAD MINIMA DE CARACTERES
        if len(codigo_confirmacion)<6:
            print("El código debe tener al menos 6 caracteres.")
            continue
        #VERIFICAR QUE NO HAYA ESPACIOS EN BLANCO. SE PUEDE USAR REPLACE(" ","")
        if " " in codigo_confirmacion:
            print("El código no puede tener espacios en blanco.")
            continue
        #VERIFICAR QUE HAYA AL MENOS UNA MAYUSCULA RECORRIENDO LA PALABRA
        mayuscula = False
        for c in codigo_confirmacion:
            if c.isupper(): #VERIFICA QUE HAYA MAYUSCULAS
                mayuscula = True
                break

        if not mayuscula:
            print("El código debe tener al menos una letra mayúscula.")
            continue

        #VERIFICAR QUE AL MENOS HAYA UN NUMERO
        numero = False
        for c in codigo_confirmacion:
            if c.isdigit(): #VERIFICA QUE SEA UN NUM NO UN STR
                numero = True
                break

        if not numero:
            print("El código debe tener al menos un número")
            continue

        break #UNA VEZ SE CUMPLA TODO, PASA A AÑADIRSE AL DICCIONARIO Y A LA LISTA

    comprador = {
        "nombre": nombre,
        "entrada": entrada,
        "codigo": codigo_confirmacion
                }

    concierto.append(comprador)
    print("Compra efectuada exitosamente!")

def consultar_comprador():
    nombre_comprador = input("Ingrese el nombre del comprador a consultar: ").lower()
    encontrado = False

    #RECORRER LA LISTA Y EVALUAR EN BASE A LA CLAVE "NOMBRE"
    for compra in concierto:
        if compra["nombre"].lower() == nombre_comprador:
            print(f"Nombre: {compra['nombre']}")
            print(f"Tipo de entrada: {compra['entrada']}")
            print(f"Código de confirmación: {compra['codigo']}")
            encontrado = True
            break

    if not encontrado:
        print("El comprador no se encuentra.")



def cancelar_compra():
    nombre_cancelar = input("Ingrese el nombre del comprador a cancelar: ").lower()
    encontrado = False

    #RECORRER LA LISTA Y EVALUAR NUEVAMENTE CON NOMBRE, PERO AQUÍ VA A AÑADIR A OTRA LISTA Y BORRAR DESPUES
    for compra in concierto:
        if compra["nombre"].lower() == nombre_cancelar:
            compras_canceladas.append(compra)  
            concierto.remove(compra)
            print("¡Compra cancelada!")
            encontrado = True
            break

    if not encontrado:
        print("No se pudo cancelar la compra.")

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

