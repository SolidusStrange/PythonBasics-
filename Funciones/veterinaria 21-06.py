def listarMascotas():
    print("-----------")
    for t in listaAnimales:
        print(t)
        print("-----------")

def agregarAnimal():
    nombre = input("Ingrese nombre")
    duenio = input("Ingrese dueño")
    tipo = input("Ingrese tipo")
    sexo = input("Ingrese sexo")
    if buscarMascota(nombre)==False:
        nueva_mascota={
            "nombre":nombre,
            "dueño": duenio,
            "tipo": tipo,
            "sexo":sexo
        }
        listaAnimales.append(nueva_mascota)
    else:
        print("La mascota existe")
    listarMascotas()

def eliminarMascota():
    flag = False
    nombre = input("Ingrese nombre")
    for temp in listaAnimales:
        if temp["nombre"]==nombre:
            listaAnimales.remove(temp)
            print("Se elimino")
            flag = True
    if flag==False:
        print("No se encontro")

def buscarMascota(nombre):
    flag = False
    for temp in listaAnimales:
        if temp["nombre"]==nombre:
            print(temp)
            flag = True
    if flag==False:
        print("No se encontro")
    return flag

def buscarHora(horaI):
    for i in hora:
        if i==horaI:
            return True
    return False
def agendarHora():
    horaT= int(input("Ingrese hora"))
    if horaT>=8 and horaT<=20:
        if buscarHora(horaT)==False:
            hora.append(horaT)
        else:
            print("Hora tomada")  
    else:
        print("Fuera de rango horario")
        
opcion =0
listaAnimales=[]
hora=[]
diccionario={}

while opcion!=6:
    try:
        print("Veterinaria Cucho")
        print("1-Agregar mascota ")
        print("2-Listar Mascotas")
        print("3-Eliminar Mascotas")
        print("4-Buscar Mascotas")
        print("5-Agendar hora")
        print("6-Salir")
        opcion = int(input("Seleccione opcion"))
    except:
        print("Ingrese la opcion correcta")
    
    if opcion==1:
        agregarAnimal()
    elif opcion==2:
        listarMascotas()
    elif opcion==3:
        eliminarMascota()
    elif opcion==4:
        nombre = input("Ingrese nombre")
        buscarMascota(nombre)
    elif opcion==5:
        agendarHora()
    elif opcion==6:
        print("Adios")
    else:
        print("Ingrese opcion correcta")
