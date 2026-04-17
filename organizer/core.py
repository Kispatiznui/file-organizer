import os
import shutil
from datetime import datetime

def get_category(extension, config):
    for category, extensions in config.items():
        if extension.lower() in extensions:
            return category
    return "others"

def organizar_archivos(ruta, config):
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            extension = archivo.split('.')[-1]
            categoria = get_category(extension, config)

            destino = os.path.join(ruta, categoria)
            os.makedirs(destino, exist_ok=True)

            shutil.move(ruta_completa, os.path.join(destino, archivo))

# 🔥 limpiar duplicados simple
def limpiar_duplicados(ruta):
    vistos = set()

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            if archivo in vistos:
                os.remove(ruta_completa)
            else:
                vistos.add(archivo)

# 🔥 organizar por fecha
def organizar_por_fecha(ruta):
    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)

        if os.path.isfile(ruta_completa):
            timestamp = os.path.getmtime(ruta_completa)
            fecha = datetime.fromtimestamp(timestamp).strftime("%Y-%m")

            destino = os.path.join(ruta, fecha)
            os.makedirs(destino, exist_ok=True)

            shutil.move(ruta_completa, os.path.join(destino, archivo))
