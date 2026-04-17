import argparse
from organizer.core import organizar_archivos

parser = argparse.ArgumentParser(description="File Organizer")
parser.add_argument("--path", required=True, help="Ruta a organizar")

args = parser.parse_args()

organizar_archivos(args.path)
