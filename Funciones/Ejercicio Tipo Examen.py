correos = []

def validar_correo(correo):
    
    #validar que no esté registrado
    if correo in correos:
        print("El correo ingresado ya está registrado")
        return False
    
    #validar que tenga al menos 6 caracteres
    if len(correo)<6:
        print("El correo debe tener al menos 6 caracteres")
        return False    
    
    if not "@" in correo:
        print("Debe contener un '@' ")
        return False
    
    #validar que haya texto antes y después
    partes = correo.split("@")
    
    if len(partes) != 2 or not partes[0] or not partes[1]:
        print("El correo debe tener texto antes y después del '@'.")
        return False
    
    #validar que contenga "@" y termine con ".com y .cl"
    if not correo.endswith((".com", ".cl")):
        print("Debe terminar con .com o .cl")
        return False
    
    #paso todos las validaciones
    print("Correo válido para registro.")  
    return True
    
def validar_contrasena(contrasena):
    #longitud minima 6 caracteres
    
    #al menos una mayuscula
    
    #al menos un digito
    
    #al menos un caracter especial
    
    #no espacios en blanco
    
    pass

def registrar_correo():
    correo = input("Ingrese el correo a registrar: ").strip().lower()
    contrasena = input("Ingrese una contraseña: ")
    
    if validar_correo(correo) and validar_contrasena(contrasena):
        correos.append(correo)
        print("Correo registrado exitosamente.\n")
        
    
        
def eliminar_correo():
    correo = input("Ingrese el correo a eliminar: ").strip().lower()
    
    if correo in correos:
        correos.remove(correo)
        print("Correo eliminado con éxito.")
    else:
        print("Correo no se encuentra registrado. Intente nuevamente.")
    

                    
def consultar_correo():
    correo = input("Ingrese el correo a consultar: ").strip().lower()
    if correo in correos:
        print("El correo está registrado.")
    else:
        print("El correo consultado no está registrado.")

def mostrar_correos():
    if correos:
        print("---CORREOS---")
        for i, correo in enumerate(correos, 1):
            print(f"{i}. {correo}")
    else:
        print("No hay correos registrados.")

def menu():
    print("----- Menú de Correos -----")
    print("1. Registrar un correo")
    print("2. Eliminar un correo")
    print("3. Consultar un correo")
    print("4. Mostrar todos los correos")
    print("5. Salir")

while True:
    menu()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        registrar_correo()
    elif opcion == "2":
        eliminar_correo()
    elif opcion == "3":
        consultar_correo()
    elif opcion == "4":
        mostrar_correos()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")