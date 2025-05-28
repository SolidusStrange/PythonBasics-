import os
from datetime import datetime

carpeta = "D:/Github/Python/Bucles"  # Cambia esto por la ruta de tu carpeta
archivo_salida = 'documentostrabajados.txt'  # Nombre del archivo de salida

# Obtener los archivos en la carpeta
archivos = [archivo for archivo in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, archivo))]

# Abrir el archivo de salida en modo de escritura
with open(archivo_salida, 'w') as f:
    # Escribir los archivos con su fecha de modificación en el archivo de texto
    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta, archivo)
        # Obtener el timestamp de la última modificación
        timestamp = os.path.getmtime(ruta_archivo)
        # Convertir el timestamp a una fecha legible
        fecha_modificacion = datetime.fromtimestamp(timestamp).strftime('%d/%m/%y - %H:%M:%S')
        # Escribir el nombre del archivo y la fecha de modificación en el archivo
        f.write(f"{archivo} - Última modificación:- {fecha_modificacion}\n")

print(f"Los archivos se han guardado en {archivo_salida}")