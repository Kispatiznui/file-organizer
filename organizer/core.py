import os
import shutil

def organizar_archivos(ruta):
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            extension = archivo.split('.')[-1]

            carpeta_destino = os.path.join(ruta, extension)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            shutil.move(ruta_completa, os.path.join(carpeta_destino, archivo))

