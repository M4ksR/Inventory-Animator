import tempfile
import shutil

from pathlib import Path

from services.video_reader import get_video_metadata
from services.frame_extractor import extract_frames
from services.strip_builder import build_strip
from services.resourcepack_builder import build_resourcepack

PROJECT_ROOT = Path(__file__).resolve().parent.parent
temp_root = PROJECT_ROOT / "temp"

temp_root.mkdir(parents=True, exist_ok=True)

def create_resourcepack(video_path, transparency, destination_folder, max_frames=10):
    with tempfile.TemporaryDirectory(dir=temp_root, prefix="build_") as temp_dir:
        workspace = Path(temp_dir)

        destination_folder = Path(destination_folder)
        if destination_folder.exists():
            raise FileExistsError("Destination folder already exists")

        frames = extract_frames(video_path, transparency, max_frames)
        strip_path = workspace / "inventory.png"
        metadata = get_video_metadata(video_path)

        expected_count = min(metadata['frame_count'], max_frames)
        if expected_count <= 0:
            raise ValueError("Video contains no frames")

        build_strip(frames, expected_count, strip_path)
        temp_pack_path = workspace / "resourcepack"
        build_resourcepack(strip_path, temp_pack_path)

        destination_folder.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(temp_pack_path, destination_folder)

        return destination_folder
