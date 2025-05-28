#acceder a lista e imprimirla con for
lista = [3,4,5,6,7,10]
for asd in lista:
    print("Con for, el número es: ", asd)

#acceder a lista e imprimirla con while
print("----------------------")
indice = 0
while indice<len(lista): #el while hasta el número máximo del indice(len(lista))
    print("While, el número es: ", lista[indice])
    indice += 1

#probar for hasta 9(sin contarlo) del 0 al 8
print("----------------------")
for i in range(9):
    print("Imprimir rango ", i)

