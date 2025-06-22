def agregarAnimal():
    nombre = input("Ingrese el nombre del animal a agregar").strip().lower() #se quitan los espacios y se vuelve minusculas
    dueno = input("Ingrese dueño").strip().lower()
    tipo = input("Ingrese el tipo de mascota").strip().lower()
    genero = input("Ingrese genero").strip().lower()
    nueva_mascota = {
        "nombre": nombre,
        "dueño": dueno,
        "tipo": tipo,
        "genero": genero,
    }
    listaAnimales.append(nueva_mascota)
    print(f"\n------AGREGADO------\nNombre: {nueva_mascota['nombre'].capitalize()}\nTipo: {nueva_mascota['tipo'].capitalize()}\n--------------------")

def listarAnimales():
    if not listaAnimales:
        print("-"*20)
        print("Aún no hay animales ingresados")
        print("-" * 20)
    else:
        print("-" * 30)
        for i, animal in enumerate(listaAnimales, 1):
            print(f"{i}.  Nombre: {animal['nombre'].capitalize()}")
            print(f"    Dueño: {animal['dueño'].capitalize()}")
            print(f"    Tipo: {animal['tipo'].capitalize()}")
            print(f"    Genero: {animal['genero'].capitalize()}")
            print("-" * 30)

def eliminarMascota():
    encontrado = False
    nombre = input("Ingrese la mascota a eliminar").lower()
    for animal in listaAnimales:
        if animal["nombre"].lower() == nombre:
            listaAnimales.remove(animal)
            print(f"Se ha eliminado de la lista el animal '{animal['nombre']}'")
            encontrado = True
            break

    if encontrado == False:
        print("No se ha encontrado la mascota en la lista")


def buscarMascota():
    encontrado = False
    nombre = input("Ingrese el nombre de la mascota a buscar: ").lower().strip()

    for animal in listaAnimales:
        if animal["nombre"].lower() == nombre:
            print("\nMascota encontrada:")
            print(f"Nombre : {animal['nombre'].capitalize()}")
            print(f"Dueño  : {animal['dueño'].capitalize()}")
            print(f"Tipo   : {animal['tipo'].capitalize()}")
            print(f"Género : {animal['genero'].capitalize()}")
            print("-" * 30)
            encontrado = True
            break

    if not encontrado:
        print(f"No se ha encontrado la mascota '{nombre}' en la lista")

def agendarHora():
    nombre = input("Ingrese el nombre de su mascota").strip().lower()
    #verificar que exista la mascota
    existe = False
    for animal in listaAnimales:
        if animal['nombre'] == nombre:
            existe = True
            break

    if not existe:
        print(f"No se encontró una mascota con el nombre '{nombre}'")
        return

    #Mostrar horas disponibls antes de pedir hora

    verHorasDisponibles()

    try:
        hora = int(input("Agende su hora (Horario de 8 a 20 hrs)"))
        if hora>=8 and hora<=20:
            #revisar si la hora esta tomada
            hora_tomada = False
            for h in horas:
                if h["hora"] == hora:
                    hora_tomada = True
                    break

            if hora_tomada:
                print(f"La hora {hora}:00 ya está tomada")
            else:
                horas.append({"hora": hora, "nombre": nombre})
                print(f"Hora {hora}:00 agendada con éxito para {nombre.capitalize()}")
        else:
            print("Ingrese una hora dentro del horario: (Horario de 8 a 20 hrs) ")
    except ValueError:
        print("Ingrese un valor númerico")

def listarHoras():
    if not horas:
        print("Aún no hay horas ingresadas")
        return

    else:
        for i in range(len(horas)):
            for j in range(i + 1, len(horas)):
                if horas[i]["hora"] > horas[j]["hora"]:
                    #intercambiar posiciones
                    horas[i], horas[j] = horas[j], horas[i]

    #Mostrar la lista ordenada
    print("\n--- Horas Agendadas ---")
    for reserva in horas:
        print(f"{reserva['hora']}:00 - {reserva['nombre'].capitalize()}")

def verHorasDisponibles():
    #lista con horas tomadas
    horas_tomadas = []
    for reserva in horas:
        horas_tomadas.append(reserva["hora"])
    #mostrar las horas que aún están disponibles
    print("\nHoras disponibles (8 a 20):")
    for h in range(8, 21):
        if h not in horas_tomadas:
            print(f"{h}:00")

opcion = 0
listaAnimales = []
horas = []
diccionario = {}


while opcion != 8:
    print("Veterinaria Cucho")
    print("1. Agregar Mascota")
    print("2. Listar Mascotas")
    print("3. Eliminar Mascotas")
    print("4. Buscar Mascotas")
    print("5. Agendar hora")
    print("6. Listar horas agendadas")
    print("7. Ver horas disponibles")
    print("8. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea"))
    except ValueError:
        print("Ingrese la opcion correcta")

    if opcion == 1:
        agregarAnimal()
    elif opcion == 2:
        listarAnimales()
    elif opcion == 3:
        eliminarMascota()
    elif opcion == 4:
        buscarMascota()
    elif opcion == 5:
        agendarHora()
    elif opcion == 6:
        listarHoras()
    elif opcion == 7:
        verHorasDisponibles()
    elif opcion == 8:
        print("Salir")
    else:
        print("Ingrese una opción válida")
