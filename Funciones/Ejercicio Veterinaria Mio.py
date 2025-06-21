def agregarAnimal():
    nombre = input("Ingrese el animal a agregar")
    dueno = input("Ingrese dueño")
    tipo = input("Ingrese tipo")
    sexo = input("Ingrese sexo")
    nueva_mascota = {
        "nombre": nombre,
        "dueño": dueno,
        "tipo": tipo,
        "sexo": sexo
    }
    listaAnimales.append(nueva_mascota)
    print(f"'{nombre}' animal y sus datos agregados.")
    
def listarAnimales():
    if not listaAnimales:
        print("No hay ningún animal agregado")
    else:
        print(f"La lista de animales es: {listaAnimales}")

def eliminarMascota():
    flag = False
    nombre = input("Ingrese la mascota a eliminar: ").lower()
    for temp in listaAnimales:
        if temp["nombre"].lower()==nombre:
            listaAnimales.remove(temp)
            print("Se ha eliminado {temp} correctamente")
            flag = True 
    if flag==False:
        print("No se encuentra en la lista")
        

def buscarMascota():
    flag = False
    nombre = input("Ingrese la mascota a eliminar: ").lower()
    for temp in listaAnimales:
        if temp["nombre"].lower()==nombre:
            print(temp)
            flag = True 
    if flag==False:
        print("No se encuentra en la lista")

def agendarHora():
    horaT = int(input("Ingrese hora"))
    if horaT>= 8 and horaT <= 20:
        if horaT in horas:
            horas.append(horaT)
            print("Hora agendada.")
        else:
            print("La hora ya está tomada.")     
    else:
        print("Hora fuera de rango.")       

opcion = 0
listaAnimales = []
horas= []
diccionario = {}

while opcion!=6:
    print("Veterinaria Cucho")
    print("1. Agregar Mascota")
    print("2. Listar Mascotas")
    print("3. Eliminar Mascotas")
    print("4. Buscar Mascotas")
    print("5. Agendar hora")
    print("6. Salir")
    try:
        opcion = int(input("Ingrese la opción que desea"))
    except ValueError:
        print("Ingrese la opcion correcta")

    if opcion == 1:
        agregarAnimal()
    elif opcion ==2:
        listarAnimales()
    elif opcion ==3:
        eliminarMascota()
    elif opcion ==4:
        buscarMascota()
    elif opcion ==5:
        agendarHora()
    elif opcion ==6:
        print("Salir")
    else:
        print("Ingrese una opción válida")
