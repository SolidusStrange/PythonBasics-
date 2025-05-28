clave_correcta = "python123"
intentos = 0
max_intentos = 3

#verificamos si la contraseña está incorrecta y no se agoten los intentos
while not clave_correcta == input("Ingrese la contraseña: ") and intentos < max_intentos:
    intentos += 1
    print(f"Contraseña incorrecta. Intento {intentos} de {max_intentos}.")
    
#verificamos si fue exitoso o no
if intentos < max_intentos:
    print("Acceso concedido.")
else:
    print("Has superado el número máximo de intentos.")
          
        