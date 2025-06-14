cursos = []
opcion = ""
contador = 0

while opcion!="n":
    nombre = input("Ingrese el nombre del alumno: ")
    direccion = input("Ingrese la dirección del alumno: ")
    telefono = input("Ingrese el teléfono del alumno: ")

    alumno = []
    alumno = [nombre, direccion, telefono]
    cursos.append(alumno)

    contador += 1
    if contador == 30:
        opcion = "n"
        print("")
    else:
       opcion = input("Desea agregar otro alumno: (s/n): ").lower()
       print("") 

for alumno in cursos:
    print("Nombre: ", alumno[0])
    print("Dirección: ", alumno[1])
    print("Teléfono: ", alumno[2])
    print("")    

