#ingresar 5 notas de 3 estudiantes una en cada lista, 
#el promedio de cada estudiante y el del curso

estudiante1 = []
estudiante2 = []
estudiante3 = []

while True:
    print("\n*****Menu*****")
    print("1. Notas y promedio del primer estudiante")
    print("2. Notas y promedio del segundo estudiante")
    print("3. Notas y promedio del tercer estudiante")
    print("4. Promedio total de los estudiantes")
    print("5. Eliminar la mejor nota de cada estudiante")
    print("6. Salir")
    
    opcion = int(input("Ingrese el número del estudiante"))

    if opcion == 1:
        if not estudiante1:
            i=0
            suma1 = 0
            while i<5:
                nota = float(input("Ingrese la nota del estudiante"))
                estudiante1.append(nota)
                i+=1
                suma1 += i 
            print(f"Las notas del estudiante son: {estudiante1}")
            prom1 = sum(estudiante1)/len(estudiante1)
            print(f"El promedio del estudiante es: {prom1}")
        else:
            print("Lista ya tiene datos")

    elif opcion == 2:
        if not estudiante2:
            i=0
            suma2 = 0
            while i<5:
                nota = float(input("Ingrese la nota del estudiante"))
                estudiante2.append(nota)
                i+=1
                suma2 += i 
            print(f"Las notas del estudiante son: {estudiante2}")
            prom2 = sum(estudiante2)/len(estudiante2)
            print(f"El promedio del estudiante es: {prom2}")
        else:
            print("Lista ya tiene datos")

    elif opcion == 3:
        if not estudiante3:
            i=0
            suma3 = 0
            while i<5:
                nota = float(input("Ingrese la nota del estudiante"))
                estudiante3.append(nota)
                i+=1
                suma3 += i
            print(f"Las notas del estudiante son: {estudiante3}")
            prom3 = sum(estudiante3)/len(estudiante3)
            print(f"El promedio del estudiante es: {prom3}")
        else:
            print("Lista ya tiene datos")

    elif opcion == 4:
        print(f"El promedio de los tres estudiantes es: {(prom1+prom2+prom3)/3}")

    elif opcion == 5:
        print("Saliendo del programa")
        break

    elif opcion == 6:
        maximo1 = max(estudiante1)
        estudiante1.remove(maximo1)
        print(estudiante1)