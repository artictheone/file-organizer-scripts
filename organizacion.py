import os
import shutil
from datetime import datetime
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

def is_alias(path: str) -> bool:
    """
    Verifica si un archivo es un alias (acceso directo) utilizando el comando osascript.

    Args:
        path (str): Ruta del archivo a verificar.

    Returns:
        bool: True si el archivo es un alias, False en caso contrario.
    """
    result = subprocess.run(['osascript', '-e', f'tell application "Finder" to original item of alias POSIX file "{path}"'], capture_output=True)
    logging.debug(f"Verificando si {path} es un alias: {result.returncode == 0}")
    return result.returncode == 0

def organize_folder(folder_path: str) -> None:
    """
    Organiza la carpeta especificada moviendo archivos y carpetas reales a una carpeta "Archive" con fecha actual.

    Args:
        folder_path (str): Ruta de la carpeta a organizar.
    """
    logging.debug(f"Organizando carpeta {folder_path}")
    archive_folder = os.path.join(folder_path, "Archive")
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_date_folder = os.path.join(archive_folder, current_date)

    logging.debug(f"Verificando si hay archivos en la carpeta {folder_path}")
    files_to_move = [item for item in os.listdir(folder_path) if item not in [".DS_Store", "Archive"]]
    logging.debug(f"Archivos detectados: {', '.join(files_to_move)}")
    if not files_to_move:
        logging.debug(f"No hay archivos en la carpeta {folder_path}. No se creará la carpeta con la fecha.")
        return

    non_alias_files = [item for item in files_to_move if not is_alias(os.path.join(folder_path, item))]
    if not non_alias_files:
        logging.debug(f"No hay archivos no-alias en la carpeta {folder_path}. No se creará la carpeta con la fecha.")
        return

    logging.debug(f"Creando carpeta Archive en {folder_path}")
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)
        logging.debug(f"Carpeta Archive creada en {folder_path}")

    logging.debug(f"Creando carpeta con la fecha {current_date} en {archive_folder}")
    if not os.path.exists(current_date_folder):
        os.makedirs(current_date_folder)
        logging.debug(f"Carpeta con la fecha {current_date} creada en {archive_folder}")

    logging.debug(f"Moviendo archivos a la carpeta con la fecha {current_date}")
    for item_name in files_to_move:
        item_path = os.path.join(folder_path, item_name)
        if is_alias(item_path):
            logging.debug(f"Skipping alias {item_name}")
            continue
        destination_path = os.path.join(current_date_folder, item_name)
        if os.path.exists(destination_path):
            base_name, extension = os.path.splitext(item_name)
            new_name = f"{base_name}_1{extension}"
            destination_path = os.path.join(current_date_folder, new_name)
            logging.debug(f"El archivo {item_name} ya existe en {current_date_folder}. Se renombrará a {new_name}.")
        try:
            shutil.move(item_path, destination_path)
            logging.debug(f"Archivo {item_name} movido a {current_date_folder}")
        except Exception as e:
            logging.error(f"Error moving file: {e}")
    logging.debug(f"Proceso completado para la carpeta {folder_path}")

def main() -> None:
    """
    Punto de entrada del script. Organiza el Escritorio y la carpeta de Descargas.
    """
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    logging.debug("Organizando Escritorio")
    organize_folder(desktop_path)

    logging.debug("Organizando Descargas")
    organize_folder(downloads_path)

if __name__ == "__main__":
    main()