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

def verificar_datos(): #para datos que no están, mostrar en pantalla 
    modelos_faltantes_en_productos = []
    for m in stock:
        if m not in productos:
            modelos_faltantes_en_productos.append(m)
            
    modelos_faltantes_en_stock = []
    for m in productos:
        if m not in stock:
            modelos_faltantes_en_stock.append(m)

    if modelos_faltantes_en_productos:
        print("⚠️ Modelos en stock que NO están en productos:")
        for m in modelos_faltantes_en_productos:
            print(f" - {m}")
        
    if modelos_faltantes_en_stock:
        print("⚠️ Modelos en productos que NO están en stock:")
        for m in modelos_faltantes_en_stock:
            print(f" - {m}")

    if not modelos_faltantes_en_productos and not modelos_faltantes_en_stock:
        print("✅ Todos los modelos están sincronizados entre productos y stock.")


def stock_marca(marca):
    encontrado = False
    total = 0
    for m in productos:
        if productos[m][0].lower() == marca:
            encontrado = True
            total += stock[m][1]    
    
    if not encontrado:
        print("La marca consultada no se encuentra en los registros")
    else:
        print(f"El total de stock de la marca {marca} es: {total}")  
    
            
def busqueda_precio(p_min, p_max):
    resultados = []

    for m in stock:
        precio = stock[m][0]
        cantidad = stock[m][1]
        if p_min<=precio<=p_max and cantidad>0:
            marca = productos[m][0]
            resultados.append(f"{marca}--{m}")
            
    if resultados:
        for r in resultados:
            print(r)
            
    else:
        print("No hay notebooks en ese rango de precios")            
            
def actualizar_precio(modelo, p):
    encontrado = False
    for m in stock:
        if m.lower() == modelo:
            encontrado = True
            stock[m][0] = p
            return True
        
    if not encontrado:
        return False 

def mostrar_sin_stock():
    sin_stock = []
    for m in stock:
        if stock[m][1] == 0:
            if m in productos: #NO ESTÁ FS1230HD EN PRODUCTOS
                marca = productos[m][0]
            else:
                marca = "Marca desconocida"
            sin_stock.append(f"{marca} -- {m}")

    if sin_stock:
        print("Modelos sin stock:")
        for s in sin_stock:
            print(s)
            
    else:
        print("Todos los modelos tienen stock disponible")
                
def modelos_bajo_stock(umbral_minimo):
    minimo = []
    for m in stock:
        precio = stock[m][1]
        if stock[m][1]<=umbral_minimo:
            if m in productos:
                marca = productos[m][0]
            else:
                marca = "Marca desconocida"
            minimo.append(f"{m} -- {marca} -- {precio}")
        
    if minimo:
        for m in minimo:
            print(m)
    
    else:
        print("No hay productos con menos del stock mínimo ingresado")

def notebook_procesador(procesador):
    lista_por_procesador = []
    for m in productos:
        if procesador.lower() in productos[m][5].lower(): #para que busque similares, ej i5 en intel core i5
            marca = productos[m][0]
            tipo_procesador = productos[m][5]
            lista_por_procesador.append(f"{marca} -- {m} -- {tipo_procesador}")
            
    if lista_por_procesador:
        for p in lista_por_procesador:
            print(p)            
    else:
        print("No se han encontrado notebooks por el procesador buscado")

def notebook_disco(disco):
    lista_por_disco = []
    for m in productos:
        if disco.lower() in productos[m][3].lower(): #para que busque similares, ej i5 en intel core i5
            marca = productos[m][0]
            tipo_disco = productos[m][3]
            lista_por_disco.append(f"{marca} -- {m} -- {tipo_disco}")
            
    if lista_por_disco:
        for p in lista_por_disco:
            print(p)            
    else:
        print("No se han encontrado notebooks por el disco buscado")
        
def agregar_modelo():
    modelo = input("Ingrese el modelo del notebook: ").strip()
    
    if modelo in productos:
        print("Ese modelo ya existe en el inventario.")
        return
    
    marca = input("Ingrese la marca: ").strip()
    pantalla = input("Ingrese el tamaño de pantalla (por ejemplo, 15.6): ").strip()
    ram = input("Ingrese la RAM (por ejemplo, 8GB): ").strip()
    disco = input("Ingrese el tipo de disco (SSD/HDD): ").strip()
    capacidad = input("Ingrese la capacidad del disco (por ejemplo, 512GB): ").strip()
    procesador = input("Ingrese el procesador: ").strip()
    video = input("Ingrese la tarjeta de video: ").strip()

    try:
        precio = int(input("Ingrese el precio del notebook: "))
        cantidad = int(input("Ingrese la cantidad en stock: "))
    except ValueError:
        print("Error: el precio y la cantidad deben ser números.")
        return

    productos[modelo] = [marca, pantalla, ram, disco, capacidad, procesador, video]
    stock[modelo] = [precio, cantidad]

    print(f"Modelo '{modelo}' agregado correctamente.")
            
def mostrar_modelo():
    mas_caro = 0
    mas_barato = 999999999
    
    for m in stock:
        precio = stock[m][0]
        cantidad = stock[m][1]
        if m in productos:
            marca = productos[m][0]
        else:
            marca = "Marca desconocida"
        
        if cantidad>0:
            if precio>mas_caro:
                mas_caro = precio
                precios_caros = []
                precios_caros.append(f"{marca} -- {m} -- {precio} -- {cantidad}")
                
            elif precio<mas_barato:
                mas_barato = precio
                precios_baratos = []
                precios_baratos.append(f"{marca} -- {m} -- {precio} -- {cantidad}")
                
    print(f"Los notebooks con mayores precios son: {precios_caros}")
    print(f"Los notebooks con menores precios son: {precios_baratos}")
    
def eliminar_modelo(modelo):
    encontrado = False
    for m in productos:
        if m.lower() == modelo.lower():
            encontrado = True
            productos.pop(m)
            if m in stock:
                stock.pop(m)
    
    if not encontrado:
        print("No se ha encontrado el modelo ingresado")
    else:
        print("Modelo eliminado")            
    
def estadisticas_inventario():
    total_cantidad = 0
    suma_precio = 0
    for m in stock:
        cantidad = stock[m][1]
        precio = stock[m][0]*stock[m][1]
        suma_precio += precio
        total_cantidad += cantidad
    
    print(f"El total de notebooks en stock es: {total_cantidad}")
    
    if total_cantidad>0:
        print(f"El promedio de precio es: {round(suma_precio/total_cantidad)}")
    else:
        print("No hay notebooks en stock")
        return
        
    integrada = 0
    for m in productos:
        if productos[m][6].lower() == "integrada":
            integrada += 1
    
    print(f"Modelos que usan tarjeta integrada: {integrada}")

def listar_modelos(marca, tipo_disco):
    lista_productos = []
    for m in productos:
        if productos[m][0].lower() == marca and productos[m][3].lower() == tipo_disco:
            lista_productos.append(m)
            
    if lista_productos:
        for p in lista_productos:
            print(p)
    else:
        print("No hay productos que cumplan con los criterios")
        return
    
#revisar esta version para evitar errores al momento de eliminar diccionarios con pop
"""def eliminar_modelo(modelo):
    modelo = modelo.lower()
    modelo_encontrado = None
    
    for m in productos:
        if m.lower() == modelo:
            modelo_encontrado = m
            break

    if modelo_encontrado:
        productos.pop(modelo_encontrado)
        stock.pop(modelo_encontrado, None)
        print("Modelo eliminado")
    else:
        print("No se ha encontrado el modelo ingresado")"""

def actualizar_stock(modelo, cantidad):
    encontrado = False
    for m in stock:
        if m.lower() == modelo:
            stock[m][1] = cantidad
            encontrado = True
            print("Stock actualizado")
            
    if not encontrado:
        print("El modelo buscado no se encuentra")
            
    
def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        print("5. Modelos sin stock")
        print("6. Verificar datos")
        print("7. Listar modelos con bajo stock")
        print("8. Buscar notebooks por procesador")
        print("9. Buscar notebooks por tipo de disco")
        print("10. Agregar un nuevo modelo al inventario")
        print("11. Mostrar el modelo más caro y más barato disponible")
        print("12. Eliminar modelo")
        print("13. Mostrar estadísticas del inventario")
        print("14. Listar modelos de una marca con tipo disco específico")
        print("15. Actualizar stock de un modelo")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion=="1":
            marca = input("Ingrese la marca a consultar su stock").lower()
            stock_marca(marca)
        elif opcion=="2":    
            try:
                while True:
                    p_min = int(input("Ingrese el valor mínimo de precios a buscar: "))
                    p_max = int(input("Ingrese el valor máximo de precios a buscar: "))
                    if p_min>p_max:
                        print("El valor mínimo no debe ser mayor que el máximo")
                    else:
                        busqueda_precio(p_min, p_max)
                        break
                
            except ValueError:
                print("Ingrese un valor numérico")

        elif opcion=="3":
            try:
                while True:
                    modelo = input("Ingrese el modelo a buscar: ").lower()            
                    p = int(input("Ingrese el valor del precio a actualizar: "))   
                    if actualizar_precio(modelo, p):
                        print("Precio actualizado")
                    else:
                        print("El modelo no existe")
                        
                    confirmacion = input("Quiere actualizar otro precio? (si/no)").lower()
                    if confirmacion == "no":
                        break
                    
            except ValueError:
                print("Ingrese un valor numérico")
                break
 
        elif opcion == "4":
            print("Programa finalizado.")
            break
        
        elif opcion == "5":
            mostrar_sin_stock()
        
        elif opcion == "6":
            verificar_datos()
        
        elif opcion == "7":
            try:
                umbral_minimo = int(input("Ingrese el umbral mínimo "))
                modelos_bajo_stock(umbral_minimo)
            except ValueError:
                print("Ingrese un valor numérico")
            
        elif opcion == "8":
            procesador = input("Ingrese el tipo de procesador que desea consultar")
            notebook_procesador(procesador)
            
        elif opcion == "9":
            disco = input("Ingrese el tipo de procesador que desea consultar")
            notebook_disco(disco)
        
        elif opcion == "10":
            agregar_modelo()
        
        elif opcion == "11":
            mostrar_modelo()
        
        elif opcion == "12":
            modelo = input("Ingrese el modelo a eliminar").lower()
            eliminar_modelo(modelo)
        
        elif opcion == "13":
            estadisticas_inventario()
        
        elif opcion == "14":
            marca = input("Ingrese la marca que desea consultar: ").lower()
            tipo_disco = input("Ingrese el tipo de disco a buscar: ").lower()
            listar_modelos(marca, tipo_disco)
            
            
        elif opcion == "15":
            try:
                modelo = input("Ingrese el modelo a actualizar").lower()
                cantidad = int(input("Ingrese la nueva cantidad a actualizar"))
                if cantidad>0:
                    actualizar_stock(modelo, cantidad)
                else:
                    print("Ingrese un valor mayor a 0")
            except ValueError:
                print("Ingrese un valor numérico")

        else:
            print("Debe seleccionar una opción válida!!")
                       
main()
        
        
