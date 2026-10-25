import shutil
from pathlib import Path

source_folder = Path("assets/resourcepack_template/")

def build_resourcepack(strip_path, destination_folder):
    strip_path = Path(strip_path)
    if not strip_path.is_file():
        raise FileNotFoundError("Animation strip not found")

    destination_folder = Path(destination_folder)
    if not source_folder.is_dir():
        raise NotADirectoryError("Source folder not found")

    inventory_path = destination_folder / "assets/minecraft/optifine/anim/inventory/inventory.png"

    shutil.copytree(source_folder, destination_folder)
    shutil.copy2(strip_path, inventory_path)
    return destination_folder
