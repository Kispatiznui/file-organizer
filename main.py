import argparse
import json
import logging
import os
from organizer.core import organizar_archivos

def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_config(path="config.json"):
    if not os.path.exists(path):
        raise FileNotFoundError("config.json not found")
    
    with open(path, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="File Organizer CLI Tool")
    parser.add_argument("--path", required=True, help="Target directory path")

    args = parser.parse_args()

    setup_logging()

    try:
        config = load_config()
        organizar_archivos(args.path, config)
        print("✅ Organization completed successfully")
    except Exception as e:
        logging.error(str(e))
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
