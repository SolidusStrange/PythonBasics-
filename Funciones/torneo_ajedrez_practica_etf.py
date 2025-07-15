participantes = []
inscritos = categoria_i = categoria_j = categoria_a = 0
elo_acum = 0

def inscribir_participante():
    global inscritos, categoria_i, categoria_j, categoria_a, elo_acum
    while True:
        nombre = input("Ingrese el nombre del participante: \n").lower()
        encontrado = False
        for p in participantes:
            if p["nombre"].lower() == nombre:
                print("El nombre ya está registrado")
                encontrado = True
                break
        
        if not encontrado:
            break    
        
    while True:
        categoria = input("Ingrese la categoria: \nI. Infantil\nJ. Juvenil\nA. Adulto\n").upper()
        if categoria == "I" or categoria == "J" or categoria == "A":
            if categoria == "I":
                categoria_i += 1
                break
            if categoria == "J":
                categoria_j += 1
                break
            if categoria == "A":
                categoria_a += 1
                break
        else:
            print("Debe ingresar una categoría válida")
            
    while True:
        codigo = input("Ingrese el código de registro: \n")
        if len(codigo)<8:
            print("Debe incluir mínimo 8 caracteres")
            continue
            
        contiene_mayuscula = False
        for c in codigo:
            if c.isupper():
                contiene_mayuscula = True
                break
            
        if not contiene_mayuscula:
            print("Debe contener al menos una mayúscula")
            continue
        
        contiene_numero = False
        for c in codigo:
            if c.isdigit():
                contiene_numero = True
                break
            
        if not contiene_numero:
            print("Debe contener al menos un número")
            continue
            
        if " " in codigo:
            print(" No debe contener espacios")
            continue    
        
        break
    
    while True:
        try: 
            elo = int(input("Ingrese su ELO: \n"))
            if 800<=elo<=2800:
                elo_acum += elo
                break
            else:
                print("Debe ingresar un valor en el rango de 800 y 2800")
            
        except ValueError:
            print("Debe ingresar un valor numérico")
            
            
    participantes.append({
        "nombre": nombre,
        "categoria": categoria,
        "codigo": codigo,
        "elo": elo
    }
    )
    print("Datos ingresados correctamente")
    inscritos += 1
    
def consultar_inscripcion():
    nombre = input("Ingrese el nombre que desea consultar: \n").lower()
    
    encontrado = False
    for n in participantes:
        if n["nombre"].lower() == nombre:
            print(f"\nNombre: {n['nombre']}")
            print(f"Categoría: {n['categoria']}")
            print(f"Código: {n['codigo']}")
            print(f"Elo: {n['elo']}")
            encontrado = True
            break
    
    if not encontrado: 
        print("No se encuentra en la base de datos el nombre consultado")
        
def cancelar_inscripcion():

    nombre = input("Ingrese el nombre del participante a eliminar: \n").lower()
    encontrado = False
    for p in participantes:
        if p["nombre"].lower() == nombre:
            participantes.remove(p)
            encontrado = True
            break
        
    if not encontrado:
        print("No se ha encontrado en la base de datos el nombre ingresado")

def ver_estadisticas():
    print(f"El total de inscripciones es: {inscritos}")
    print(f"Cantidad por categoria: \nCategoría Adulto: {categoria_a}\nCategoría Infantil: {categoria_i}\nCategoría Juvenil: {categoria_j}")
    if inscritos > 0:
        promedio = elo_acum / inscritos
    else:
        promedio = 0
    print(f"Promedio de ELO de jugadores inscritos: {promedio:.2f}")

def exportar_inscritos():
    pass

def mostrar_menu():
    print("\nMENÚ PRINCIPAL")
    print("1.- Inscribir participante")
    print("2.- Consultar inscripción")
    print("3.- Cancelar inscripción")
    print("4.- Ver estadísticas")
    print("5.- Exportar inscritos")
    print("6.- Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: \n")

        if opcion == "1":
            inscribir_participante()
        elif opcion == "2":
            consultar_inscripcion()
        elif opcion == "3":
            cancelar_inscripcion()
        elif opcion == "4":
            ver_estadisticas()
        elif opcion == "5":
            exportar_inscritos()
        elif opcion == "6":
            print("Sistema cerrado. ¡Buena suerte a los participantes!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
