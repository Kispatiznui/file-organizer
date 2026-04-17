import os
import shutil
import logging

def get_category(extension, config):
    for category, extensions in config.items():
        if extension.lower() in extensions:
            return category
    return "others"

def organizar_archivos(ruta, config):
    if not os.path.exists(ruta):
        raise ValueError("Invalid path")

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            extension = archivo.split('.')[-1]

            categoria = get_category(extension, config)
            carpeta_destino = os.path.join(ruta, categoria)

            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)

            destino_final = os.path.join(carpeta_destino, archivo)

            shutil.move(ruta_completa, destino_final)

            logging.info(f"Moved: {archivo} → {categoria}")
