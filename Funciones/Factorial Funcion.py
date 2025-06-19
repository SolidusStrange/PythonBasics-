def factorial(n): #pasamos el argumento "n"
    if n==0: #evaluamos que "n" sea 0
        return 1 #si es 0, devuelve 1
    return factorial(n-1)*n #si no se ejecuta la devolución 1, se hace una funcion recursiva llamando a la misma función pero con (n-1)*m
#al ser n-1, significa que en algún momento la n será 0 y ahí terminará la función ya que se acabará la recursividad

x = int(input("Ingrese numero"))

print(factorial(x))
