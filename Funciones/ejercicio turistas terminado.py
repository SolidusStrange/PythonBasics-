turistas = [
    {"nombre": "John Doe", "pais": "Estados Unidos", "fecha": "12-01-2024"},
    {"nombre": "Emily Smith", "pais": "Estados Unidos", "fecha": "23-03-2024"},
    {"nombre": "Michael Brown", "pais": "Estados Unidos", "fecha": "05-07-2023"},
    {"nombre": "Jessica Davis", "pais": "Estados Unidos", "fecha": "15-11-2024"},
    {"nombre": "Carlos Garcia", "pais": "Mexico", "fecha": "10-05-2024"},
    {"nombre": "Maria Lopez", "pais": "Mexico", "fecha": "08-12-2023"},
    {"nombre": "Joao Silva", "pais": "Brasil", "fecha": "20-06-2024"},
    {"nombre": "Ana Santos", "pais": "Brasil", "fecha": "03-10-2023"},
    {"nombre": "Martin Fernandez", "pais": "Argentina", "fecha": "13-02-2023"},
    {"nombre": "Sofia Gomez", "pais": "Argentina", "fecha": "07-04-2024"},
    {"nombre": "Julian Martinez", "pais": "Argentina", "fecha": "19-09-2023"},
    {"nombre": "Agustin Morales", "pais": "Argentina", "fecha": "28-03-2024"}
]

def turistas_por_pais(pais):
    encontrado = False
    pais = pais.lower()
    for turista in turistas:
        if turista["pais"].lower() == pais:
            print(f"Nombre: {turista['nombre']}, País: {turista['pais']}, Fecha de ingreso: {turista['fecha']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron turistas en ese país.")


def turistas_por_mes(mes):
    total_turistas = len(turistas) #el largo de la lista para el %
    contador_mes = 0

    for turista in turistas:
        mes_turista = int(turista["fecha"][3:5]) #extrae de la fecha exactamente el mes y lo transforma a entero quitando el 0
        if mes_turista == mes:
            contador_mes += 1

    if contador_mes > 0:
        porcentaje = round((contador_mes/total_turistas)*100,1) #round(variable,cantidad decimales)
        return porcentaje
    else:
        return 0.0 #si no es mayor que cero, devolverá 0.0%

def eliminar_turista():
    turista_eliminado = input("Ingrese el turista a eliminar de la lista.").lower()
    encontrado = False
    for turista in turistas:
        if turista["nombre"].lower() == turista_eliminado:
            turistas.remove(turista)
            print(f"El turista {turista['nombre']} ha sido eliminado con éxito")
            encontrado = True
            break

    if not encontrado:
        print("Turista no encontrado. No se pudo eliminar")

while True:
    print("MENU PRINCIPAL")
    print("1. Turistas por país")
    print("2. Turista por mes")
    print("3. Eliminar turista")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese la opción que desea: "))
    except ValueError:
        print("Ingrese un valor numérico")
        continue

    if opcion == 1:
        pais = input("Ingrese el país a listar: ")
        turistas_por_pais(pais)

    elif opcion == 2:
        while True:
            try:
                mes = int(input("Ingrese el número del mes que desea contar: "))
                if mes>=1 and mes<=12:
                    porcentaje = turistas_por_mes(mes)
                    print(f"El {porcentaje}% de los turistas visitó Chile en el mes {mes}.\n")
                    break
                else:
                    print("Ingrese número dentro del rango de meses(1 a 12).")
            except ValueError:
                print("Ingrese un valor numérico.")

    elif opcion == 3:
        eliminar_turista()

    elif opcion == 4:
        print("Programa terminado...")
        break

    else:
        print("Ingrese una opción válida")
