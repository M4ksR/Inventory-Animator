import cv2
from pathlib import Path

from services.frame_processor import (resize_frame,
                                      apply_transparency,
                                      overlay_inventory)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
template_path = PROJECT_ROOT / "assets/templates/inventory_overlay.png"

def extract_frames(video_path, transparency=100, max_frames=10, progress_callback=None):
    capture = cv2.VideoCapture(video_path)

    try:
        if not capture.isOpened():
            raise ValueError("Can not open file")

        template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
        if template is None:
            raise ValueError("Can not open template")

        success, frame = capture.read()
        count = 0

        while count < max_frames and success:
            # приведем изображение к нужному размеру
            processed_frame = resize_frame(frame)

            # применим установленную прозрачность
            processed_frame = apply_transparency(processed_frame, transparency)

            # произведем наложение картинки на шаблон
            processed_frame = overlay_inventory(processed_frame, template)

            # функция для подсчета готовых кадров
            if progress_callback is not None:
                progress_callback(count + 1)

            # вернем готовый кадр наружу
            yield processed_frame

            # получим новый кадр и увеличим счетчик
            success, frame = capture.read()
            count += 1

    finally:
        capture.release()
