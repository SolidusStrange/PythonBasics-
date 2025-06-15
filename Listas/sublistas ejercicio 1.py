"""Crea un programa que registre 3 alumnos.
Por cada alumno, guarda el nombre y su nota en una sublista.
Al final, muestra todos los alumnos con sus notas y cuántos aprobaron (nota ≥ 60)."""

alumnos = []

#registrar 3 alumnos
for i in range(3):
    print(f"\nAlumno {i+1}")
    nombre = input("Ingrese el nombre del alumno")
    nota = float(input("Ingrese la nota del alumno"))
    alumnos.append([nombre, nota])

#mostrar alumnos y contar aprobados
print("\nLista de alumnos y notas:")
aprobados = 0

for alumno in alumnos:
    print(f"{alumno[0]} - Nota: {alumno[1]}")
    if alumno[1]>=60:
        aprobados += 1

print(f"La cantidad de alumnos aprobados es: {aprobados}")
