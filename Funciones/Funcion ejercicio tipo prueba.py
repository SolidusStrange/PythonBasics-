participantes = []

def inscribir_participante():
    #NOMBRE DEL PARTICIPANTE
    while True:
        nombre = input("Ingrese su nombre: \n")
        encontrado = False
        for n in participantes:
            if n["nombres"] == nombre:
                print("No se pueden inscribir nombres repetidos.")
                encontrado = True
                break
        if not encontrado:
            break

    #SOLICITAR CATEGORÍA
    while True:
        categoria = input("Ingrese la categoría ('A o M')\n").lower()
        if categoria == "a" or categoria == "m":
            break
        else:
            print("Debe ingresar una categoria válida")

    #CODIGO DE INSCRIPCION
    while True:
        codigo = input("Ingrese el codigo de inscripcion:\n")

        #AL MENOS 8 CARACTERES
        if len(codigo) < 8:
            print("Debe tener al menos 8 caracteres")
            continue

        #UNA MAYUSCULA
        
        CONTIENE_MAYUSCULA = False
        for caracter in codigo:
            if caracter.isupper():
                CONTIENE_MAYUSCULA = True
                break

        if not CONTIENE_MAYUSCULA:
            print("Debe tener al menos una mayuscula")
            continue

        #AL MENOS UN NUMERO

        CONTIENE_NUMERO = False
        for caracter in codigo:
            if caracter.isdigit():
                CONTIENE_NUMERO = True
                break

        if not CONTIENE_NUMERO:
            print("Debe tener al menos un numero")
            continue

        #SIN ESPACIOS
        if " " in codigo:
            print("No debe contener espacios")
            continue

        print("Validaciones exitosas. Codigo ingresado")
        break

    participantes.append({
        "nombres": nombre,
        "categoria": categoria,
        "codigo": codigo
    })

    print("Datos del participante ingresados correctamente.")

def consultar_inscripcion():
    nombre = input("Ingrese el nombre a consultar: ").lower()
    encontrado = False
    for n in participantes:
        if n["nombres"].lower() == nombre:
            print(f"Nombre: {n['nombres']}")
            print(f"Categoría: {n['categoria']}")
            print(f"Código: {n['codigo']}")
            encontrado = True
            break

    if not encontrado:
        print("El participante no está inscrito")

def cancelar_inscripcion():
    nombre = input("Ingrese el nombre a cancelar: ").lower()
    encontrado = False
    for n in participantes:
        if n["nombres"].lower() == nombre:
            participantes.remove(n)
            print("Inscripción cancelada")
            encontrado = True
            break

    if not encontrado:
        print("No se pudo cancelar la inscripción")

def menu():
    print("Menu Principal")
    print("1. Inscribir participante")
    print("2. Consultar inscripción")
    print("3. Cancelar inscripción")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese la opción que desea: \n")
        
        if opcion == "1":
            inscribir_participante()
        
        elif opcion == "2":
            consultar_inscripcion()
        
        elif opcion == "3":
            cancelar_inscripcion()
        
        elif opcion == "4":
            print("Gracias por participar. ¡Nos vemos en la carrera!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente")

main()


    
