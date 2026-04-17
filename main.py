import argparse
import json
from organizer.core import organizar_archivos, limpiar_duplicados, organizar_por_fecha

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="File Organizer CLI")

    parser.add_argument("--path", required=True)
    parser.add_argument("--mode", choices=["organize", "clean", "date"], default="organize")

    args = parser.parse_args()
    config = load_config()

    if args.mode == "organize":
        organizar_archivos(args.path, config)

    elif args.mode == "clean":
        limpiar_duplicados(args.path)

    elif args.mode == "date":
        organizar_por_fecha(args.path)

    print("✅ Done")

    main()
