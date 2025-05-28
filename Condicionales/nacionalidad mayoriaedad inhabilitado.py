# Ingreso de datos
edad = int(input("Ingrese su edad: "))
nacionalidad = input("¿Es chileno o residente? (chileno/residente/otro): ").lower()
inhabilitado = input("¿Está inhabilitado legalmente? (sí/no): ").lower() == "sí"

# Validación
while edad < 18 or (nacionalidad != "chileno" and nacionalidad != "residente") or inhabilitado:
    print("No cumple con los requisitos para acceder al beneficio.")
    print("Ingrese los datos nuevamente.\n")

    # Se vuelven a pedir los datos
    edad = int(input("Ingrese su edad: "))
    nacionalidad = input("¿Es chileno o residente? (chileno/residente/otro): ").lower()
    inhabilitado = input("¿Está inhabilitado legalmente? (sí/no): ").lower() == "sí"

print("¡Acceso al beneficio concedido!")
