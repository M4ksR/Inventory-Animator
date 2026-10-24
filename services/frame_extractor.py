import cv2
from pathlib import Path

from services.frame_processor import (resize_frame,
                                      apply_transparency,
                                      overlay_inventory)

template_path = Path("assets/templates/inventory_overlay.png")

def extract_frames(video_path,
                   transparency=50,
                   max_frames=100):

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

            # вернем готовый кадр наружу
            yield processed_frame

            # получим новый кадр и увеличим счетчик
            success, frame = capture.read()
            count += 1

    finally:
        capture.release()
