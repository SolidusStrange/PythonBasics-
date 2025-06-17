def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n

x = int(input("Ingrese numero"))

print(factorial(x))