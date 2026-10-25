import cv2
import numpy as np

from PIL import Image

FRAME_WIDTH = 704
FRAME_HEIGHT = 664

# функция, изменяющая размер изображения под размер шаблона инвентаря
def resize_frame(frame):
    return cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

def apply_transparency(frame, transparency):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    alpha = round(255 * transparency / 100)
    frame[:, :, 3] = alpha
    return frame

def overlay_inventory(frame, template):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGBA)
    template = cv2.cvtColor(template, cv2.COLOR_BGRA2RGBA)

    img1 = Image.fromarray(frame)
    img2 = Image.fromarray(template)

    result = Image.alpha_composite(img1, img2)
    result = np.array(result)
    return cv2.cvtColor(result, cv2.COLOR_RGBA2BGRA)
