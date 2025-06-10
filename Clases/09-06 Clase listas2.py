nombres = ["Juan", "Pedro", "Diego"]
gatos = ["Misifu", "Firulais", "Cachupin"]

print("\nUnir listas con extend")
nombres.extend(gatos)
print(nombres)

print("\nEliminar el ultimo con pop")
nombres.pop()
print(nombres)

print("\nInvertir la lista con reverse")
nombres.reverse()
print(nombres)

print("\nOrdenar la lista alfabeticamente con Sort")
nombres.sort()
print(nombres)

print("\nAgregar al final con Append")
nombres.append("Michi")
print(nombres)

print("\nRemover la primera ocurrencia")
nombres.remove("Juan")
print(nombres)