usuario1=None 
usuario2=None 
usuario3=None
contrasena1=None 
contrasena2=None 
contrasena3=None
usuarios = [usuario1, usuario2, usuario3]
contraseñas = [contraseña1, contraseña2, contraseña3]

while True #menu
  print("---------------------")
  print("1. Iniciar sesion")
  print("2. Registrar usuario")
  print("3. Salir")
  try: 
    opcion = int(input("Ingrese una opción"))
  except ValueError:
    print("Ingrese un valor númerico")
  print("---------------------")

  if opcion==1: #Iniciar sesion
    if usuarios[0] is None and usuarios[1] is None and usuarios[2] is None:
      print("No existe ningún usuario registrado. Debe registrar un usuario primero.")
    else:
      nombre=input("Ingrese su nombre de usuario")
      clave=input("Ingrese su contraseña")

      for e in range(len(usuarios)):
        if usuarios[e] == nombre and contraseñas[e] ==


      while True:
        print("---------------------")
        print("1. Realizar llamada")
        print("2. Enviar correo electrónico")
        print("3. Salir")

        try: 
          inicioMenu = int(input("Ingrese una opción"))
        except ValueError:
          print("Ingrese un valor númerico")
        print("---------------------")

        if inicioMenu==1: #realizar llamada
          numero_cel = int(input("Ingrese su número de celular: "))
                           
        elif inicioMenu==2: #enviar correo electronico
          pass 
        elif inicioMenu==3: #cerrar sesión   
          print("Cerrando sesión...")
          break
        else:
          print("Ingrese una opción válida")

  elif opcion==2: #registrar usuario
    for i in range(len(usuarios)): #rango maximo el for. Se usa range porque vamos a modificar valores de la lista
        if usuarios[i] is None: #revisar que no tenga nada ingresado
            usuarios[i] = input("Ingrese nombre de usuario: ") #se añade un valor a usuarios
            contraseñas[i] = input("Ingrese contraseña: ") #se añade una contraseña a ese usuario
            print("Usuario registrado exitosamente.")
            break #se cierra este for
          
  elif opcion==3:
    print("Saliendo del programa")
    break

  else:
    print("Ingrese una opción válida")

   
  
  
