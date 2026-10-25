import tempfile
import shutil

from pathlib import Path

from services.video_reader import count_video_frames
from services.frame_extractor import extract_frames
from services.strip_builder import build_strip
from services.resourcepack_builder import build_resourcepack

def create_resourcepack(video_path, transparency, destination_folder, max_frames=500, progress_callback=None):
    def report_progress(count):
        if progress_callback is not None:
            progress_callback(count, expected_count)

    with tempfile.TemporaryDirectory(prefix="inventory_build_") as temp_dir:
        workspace = Path(temp_dir)

        destination_folder = Path(destination_folder)
        if destination_folder.exists():
            raise FileExistsError("Ресурс-пак с таким именем уже создан")

        expected_count = count_video_frames(video_path, max_frames)

        if expected_count <= 0:
            raise ValueError("Видео не содержит кадров")

        frames = extract_frames(video_path, transparency, expected_count, progress_callback=report_progress)
        strip_path = workspace / "inventory.png"

        build_strip(frames, expected_count, strip_path)
        temp_pack_path = workspace / "resourcepack"
        build_resourcepack(strip_path, temp_pack_path)

        destination_folder.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(temp_pack_path, destination_folder)

        return destination_folder
