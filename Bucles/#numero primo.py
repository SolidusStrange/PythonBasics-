#numero primo
contador = primos = no_primos = 0

while True:
  try:
    cantidad = int(input("Ingrese la cantidad de números a verificar: "))
  except ValueError:
    print("Ingrese un valor númerico")
    continue
    
  if (cantidad/round(cantidad))==1:
    break
  else:
    print("Valor ingresado no es un entero")

while contador<cantidad:
  try:
    numero = int(input("Ingresa número: "))
  except ValueError:
    print("Ingrese un valor numérico")
    
  es_primo = True #bandera

  #verificar si es numero primo
  if numero >= 2:
      for i in range(2, numero):          
          if numero % i == 0:             
              es_primo = False
              break
  else:   
      es_primo = False
      
  #resultados
  if es_primo:
      print(numero, "es primo")
      primos += 1
  else:
      print(numero, "no es primo.")
      no_primos +=1

  contador += 1 #suma uno al contador
    
print(f"Se ingresaron {primos} números primos")
print(f"Se ingresaron {no_primos} números primos")
