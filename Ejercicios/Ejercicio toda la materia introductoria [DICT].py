# Diccionario principal
estudiantes = {}

# ------------------------------
# Funciones
# ------------------------------
def registrar_estudiante():
    
    # Registro de nombre
    nombre = input("Ingrese su nombre: ").capitalize()
    
    # Registro de edad
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
        except ValueError:
            print("Ingrese un valor entero. Intente nuevamente.")
            continue
        break
        
    asignaturas = []
    # Registro de asignaturas (listas)
    while True:
        asignatura = input("Ingrese sus asignaturas: (0 para parar)")
        if asignatura == "0":
            if not asignaturas:
                print("Debe ingresar al menos una asignatura.")
                continue
            break
        asignaturas.append(asignatura)
                        
    # SISTEMA PARA VARIAS NOTAS
    # notas_dict = {}
    # while True:
    #     asignatura = input("Ingresa la asignatura (o 'salir' para terminar): ")
    #     if asignatura.lower() == "salir":
    #         break
    #     try:
    #         nota = float(input(f"Ingresa la nota para {asignatura}: "))
    #     except ValueError:
    #         print("Ingrese un valor numérico. Intente nuevamente")
    #         continue

    #     # Si la asignatura ya está en el diccionario, añade la nota a la lista
    #     if asignatura in notas_dict:
    #         notas_dict[asignatura].append(nota)
    #     else:
    #         print("La asignatura no está registrada. Ingrese nuevamente")
    #         continue

    #     print(f"Notas actuales: {notas_dict}\n")

    # print("Notas finales:", notas_dict)
    
    # Registro de una nota por asignatura
    notas_dict = {}
    for asignatura in asignaturas:
        while True:
            try:
                nota = float(input(f"Ingrese la nota para {asignatura}: "))
                notas_dict[asignatura] = nota
                break
            except ValueError:
                print("Ingrese un valor numérico. Intente nuevamente.")
                
    # Guardar estudiante en el diccionario principal
    estudiantes[nombre] = {
        "edad":edad,
        "asignaturas":asignaturas,
        "notas":notas_dict
     
    }
    
    print(f"El estudiante {nombre} ha sido registrado con éxito.\n")    
    

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    
    print("\n=== Lista de estudiantes registrados ===")
    for nombre, datos in estudiantes.items(): # itera sobre el nombre (clave) y los datos (diccionario).
        print(f" Nombre: {nombre}") # nombre es la llave que tiene el diccionario a iterar
        print(f" Edad: {datos['edad']}") # para acceder se usa la variable datos['edad'] 
        print(f" Asignaturas: {', '.join(datos['asignaturas'])}") # convierte la lista de asignaturas en un string separado por comas
        print(" Notas:")
        for asignatura, nota in datos["notas"].items(): # Acá nos debería mostrar el par key-value. Que hay en datos["notas"], que sería "notas":notas_dict, desde ahí debería iterar mostrando lo que queremos
            print(f"       {asignatura}: {nota}") # lo iterado antes mostra. Asignatura y su respectiva nota
        print("-" * 40)   
        
def buscar_estudiante():
    pass  # Aquí irás escribiendo el código para buscar un estudiante por nombre

def promedio_estudiante():
    pass  # Aquí irás escribiendo el código para calcular el promedio de un estudiante

def eliminar_estudiante():
    pass  # Aquí irás escribiendo el código para eliminar un estudiante

# ------------------------------
# Menú principal
# ------------------------------
def menu():
    while True:
        print("=== MENÚ ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Promedio de estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            buscar_estudiante()
        elif opcion == "4":
            promedio_estudiante()
        elif opcion == "5":
            eliminar_estudiante()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")

# Ejecutar programa
menu()


