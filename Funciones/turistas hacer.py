turistas = {
    "nombre": "John Doe", "pais": "Estados Unidos", "fecha": "12-01-2024",
    "nombre": "Emily Smith", "pais": "Estados Unidos", "fecha": "23-03-2024",
    "nombre": "Michael Brown", "pais": "Estados Unidos", "fecha": "05-07-2023",
    "nombre": "Jessica Davis", "pais": "Estados Unidos", "fecha": "15-11-2024",
    "nombre": "Carlos Garcia", "pais": "Mexico", "fecha": "10-05-2024",
    "nombre": "Maria Lopez", "pais": "Mexico", "fecha": "08-12-2023",
    "nombre": "Joao Silva", "pais": "Brasil", "fecha": "20-06-2024",
    "nombre": "Ana Santos", "pais": "Brasil", "fecha": "03-10-2023",
    "nombre": "Martin Fernandez", "pais": "Argentina", "fecha": "13-02-2023",
    "nombre": "Sofia Gomez", "pais": "Argentina", "fecha": "07-04-2024",
    "nombre": "Julian Martinez", "pais": "Argentina", "fecha": "19-09-2023",
    "nombre": "Agustin Morales", "pais": "Argentina", "fecha": "28-03-2024"
}

def turistas_por_pais():
    encontrado = False
    pais = input("Ingrese el país a listar: ")
    for paises in turistas:
        if paises["pais"] == pais:
            print(paises)
            encontrado = True

    if encontrado == False:
        print("País no encontrado")

def turistas_por_mes():
    pass

def eliminar_turista():
    pass

opcion = 0
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

    if opcion==1:
        turistas_por_pais()
            
    elif opcion==2:
        turistas_por_mes()
    
    elif opcion==3:
        eliminar_turista()
            
    elif opcion==4:
        print("Saliendo del programa")
        break
