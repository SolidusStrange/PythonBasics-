# reservas_cocina.py

reservas = []
reservas_anuladas = []

def registrar_reserva():
    while True:  
        nombre = input("Ingrese el nombre del asistente: ").lower().strip()
        nombre_duplicado = False

        for asistente in reservas:
            if asistente["nombre"].lower() == nombre:
                print("El nombre ingresado ya está registrado. Ingrese uno diferente.")
                nombre_duplicado = True
                break

        if not nombre_duplicado:
            break

    while True:
        dia = input("Ingrese el día del taller (lunes, martes o miércoles): ").lower().strip()
        if dia not in ["lunes", "martes", "miercoles"]:
            print("Día ingresado no está en el horario. Intente nuevamente.")
            continue
        break

    while True:
        confirmacion = input("Ingrese clave de confirmación: ")

        # Validar longitud mínima
        if len(confirmacion) < 5:
            print("La clave debe tener al menos 5 caracteres.")
            continue

        # Validar al menos un número
        tiene_numero = False
        for c in confirmacion:
            if c.isdigit():
                tiene_numero = True
                break
        if not tiene_numero:
            print("La clave debe contener al menos un número.")
            continue

        # Validar al menos una letra
        tiene_letra = False
        for c in confirmacion:
            if c.isalpha():
                tiene_letra = True
                break
        if not tiene_letra:
            print("La clave debe contener al menos una letra.")
            continue

        # Validar que no tenga espacios
        if " " in confirmacion:
            print("La clave no debe tener espacios.")
            continue

        # Validar que no tenga caracteres especiales
        tiene_especial = False
        for c in confirmacion:
            if not c.isalnum():
                tiene_especial = True
                break
        if tiene_especial:
            print("La clave no debe tener caracteres especiales.")
            continue

        # Si pasa todas las validaciones, salir del bucle
        break

    asistentes = {
        "nombre": nombre,
        "dia": dia,
        "clave": confirmacion
    }

    reservas.append(asistentes)
    print("Reserva registrada con éxito.")
    
def consultar_reserva():
  nombre = input("Ingrese el nombre de la reserva que desea consultar: ").lower().strip()
  encontrado = False
  for reserva in reservas:
    if reserva["nombre"].lower() == nombre:
      print(f"Nombre: {reserva['nombre'].capitalize()}")
      print(f"Dia:{reserva['dia'].capitalize()} ")
      print(f"Codigo de confirmación: {reserva['clave']}:")
      encontrado = True
      break
      
  if not encontrado:
    print("No se ha encontrado la reserva consultada")

      
def anular_reserva():
  nombre = input("Ingrese el nombre de la reserva que desea anular: ").lower().strip()
  encontrado = False
  for reserva in reservas:
    if reserva["nombre"].lower() == nombre:
      encontrado = True
      reservas_anuladas.append(reserva)
      reservas.remove(reserva)
      print("Reserva anulada con éxito")
      break
      
  if not encontrado:
    print("No se ha encontrado la reserva para anular")

def mostrar_menu():
    print("MENÚ PRINCIPAL")
    print("1. Registrar reserva")
    print("2. Consultar reserva")
    print("3. Anular reserva")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_reserva()
        elif opcion == "2":
            consultar_reserva()
        elif opcion == "3":
            anular_reserva()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida.")

if __name__ == "__main__":
    main()
