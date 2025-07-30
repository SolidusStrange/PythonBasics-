#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

marcas_disponibles = []
for modelo in productos:
    marca = productos[modelo][0]
    marcas_disponibles.append(marca.lower())

def stock_marca(marca):
    total = 0
    for modelo in productos:
        if productos[modelo][0].lower() == marca:
            total += stock[modelo][1]
    print(f"Stock total de la marca {marca}: {total}")
    
def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo in stock:
        precio = stock[modelo][0]
        cantidad = stock[modelo][1]
        if p_min<=precio<=p_max and cantidad>0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}--{modelo}")        
            
    if resultados:
        resultados.sort()
        for r in resultados:
            print(r)
            
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    encontrado = False
    for m in stock:
        if m == modelo:
            stock[m][0] = p
            encontrado = True
            return True
            
    if not encontrado:
        return False

while True:
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        marca = input("Ingrese la marca que desea buscar").lower()
        if marca in marcas_disponibles:
            stock_marca(marca)
        else:
            print("La marca no está en la lista de marcas disponibles")
        
    elif opcion == "2":
        # pedir precios, validar enteros y llamar a búsqueda_precio(pmin, pmax)
        while True:
            try:
                p_min = int(input("Ingrese el valor del precio mínimo: \n"))
                p_max = int(input("Ingrese el valor del precio máximo: \n"))
                if p_min>p_max:
                    print("El precio mínimo no puede ser mayor que el máximo") 
                else:
                    busqueda_precio(p_min, p_max)
                    break
            except ValueError:
                print("Debe ingresar un valor numérico.\n")
        
    elif opcion == "3":
        # pedir modelo y nuevo precio, llamar a actualizar_precio(...)
        while True:
            try:
                modelo = input("¿Cuál modelo desea actualizar su precio?")
                p = int(input("Ingrese el precio que desea actualizar: "))
                if actualizar_precio(modelo,p):
                    print("Precio actualizado")
                else:
                    print("El modelo no existe!!")
                    
                confirmacion = input("Desea actualizar otro precio de notebook? (si/no)").lower()
                if confirmacion == "no":
                    break        
            except ValueError:
                print("Ingrese un valor numérico.")
        
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")
