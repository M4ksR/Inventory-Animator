import png
import cv2

from pathlib import Path
from contextlib import closing
from services.frame_processor import FRAME_WIDTH, FRAME_HEIGHT

# генератор, преобразующий кадры в последовательность строк
def rows_generator(frames):
    for frame in frames:
        if frame.shape != (FRAME_HEIGHT, FRAME_WIDTH, 4):
            raise ValueError("Invalid frame size or format")

        rgba_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
        for row in rgba_frame:
            yield row.reshape(-1).tobytes()

# функция сборки всех кадров в единую вертикальную ленту
def build_strip(frames, frame_count, output_path):
    if frame_count <= 0:
        raise ValueError("Frame count must be positive")

    save_path = Path(output_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    writer = png.Writer(
        width=FRAME_WIDTH,
        height=FRAME_HEIGHT * frame_count,
        alpha=True,
        greyscale=False,
        bitdepth=8
    )

    with closing(frames):
        try:
            with open(save_path, "wb") as output:
                writer.write(output, rows_generator(frames))
        except Exception:
            save_path.unlink(missing_ok=True)
            raise

    return save_path
