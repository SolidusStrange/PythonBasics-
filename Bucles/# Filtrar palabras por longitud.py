# Filtrar palabras por longitud

#lista con las palabras
palabras = ["computadora", "sol", "python", "agua", "inteligencia", "cielo"]

n = int(input("Mostrar palabras con más de cuantas letras? "))

for palabra in palabras:
    if len(palabra) > n:
        print(palabra)
        
        