"""Crea una lista vacía. Pide al usuario que ingrese productos 
hasta que escriba "fin". Luego imprime la lista completa."""

lista_compras = []
compra = ""

while compra!="fin":
    compra = input("Ingrese productos").lower()
    if compra!="fin":
        lista_compras.append(compra)
        
print("Tu lista de compras: ")
for item in lista_compras:
    print("-", item)
    
    