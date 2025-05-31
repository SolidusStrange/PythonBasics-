usuario1=None 
usuario2=None 
usuario3=None
contrasena1=None 
contrasena2=None 
contrasena3=None
usuarios = [usuario1, usuario2, usuario3]
contraseñas = [contrasena1, contrasena2, contrasena3]

while True: #menu
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
    else: #ingreso de usuario. revisar si está en la lista
      nombre=input("Ingrese su nombre de usuario")
      clave=input("Ingrese su contraseña")
      
      encontrado = False
      for e in range(len(usuarios)):
        if usuarios[e] == nombre and contraseñas[e] == clave: 
          print("Inicio de sesión exitoso")
          encontrado = True
          break
      if not encontrado: #si no encuentra nada
        print("Usuario o contraseña incorrectos.")
        continue #vuelve al menu principal
        
      while True:
        print("---------------------")
        print("1. Realizar llamada")
        print("2. Enviar correo electrónico")
        print("3. Salir")
        try: 
          inicioMenu = int(input("Ingrese una opción: "))
        except ValueError:
          print("Ingrese un valor númerico.")
        print("---------------------")
        
        if inicioMenu==1: #realizar llamada
          numero_cel = input("Ingrese su número de celular: ")
          #isdigit() para asegurarte de que solo contiene dígitos
          #len() para verificar que tenga 9 caracteres 
          #startswith("9") para confirmar que empieza con 9
          if numero_cel.isdigit() and len(numero_cel) == 9 and numero_cel.startswith("9"):
            print("Número válido.") 
          else:
            print("Número inválido. Debe comenzar con 9 y tener 9 dígitos.")               
                                
        elif inicioMenu==2: #enviar correo electronico
          while True:
            correo = input("Ingrese su correo electrónico: ")
            tiene_arroba = False
            for caracter in correo: #for en caracter y caracter del correo ingresado, iteracion en cada uno
              if caracter == "@":
                tiene_arroba = True
                break # no hace falta seguir buscando
              
            if tiene_arroba:
              break # salir del while si el correo es válido
            
            else:
              print("Correo inválido. Debe contener al menos un '@'. Intente nuevamente.")
        
          mensaje = input("Escriba el mensaje a enviar: ")
          print("Correo y mensaje guardados correctamente.")
        
        elif inicioMenu==3: #cerrar sesión   
          print("Cerrando sesión...")
          break
        else:
          print("Ingrese una opción válida.")

  elif opcion==2: #registrar usuario
    for i in range(len(usuarios)): #rango maximo el for. Se usa range porque vamos a modificar valores de la lista
        if usuarios[i] is None: #revisar que no tenga nada ingresado
            usuarios[i] = input("Ingrese nombre de usuario: ") #se añade un valor a usuarios
            contraseñas[i] = input("Ingrese contraseña: ") #se añade una contraseña a ese usuario
            print("Usuario registrado exitosamente.")
            break #se cierra este for
          
  elif opcion==3:
    print("Saliendo del programa.")
    break

  else:
    print("Ingrese una opción válida.")

   
  
  
