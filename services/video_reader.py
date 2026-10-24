import cv2

def get_video_metadata(path):
    capture = cv2.VideoCapture(path)
    try:
        if not capture.isOpened():
            raise ValueError("Can not open file")

        fps = capture.get(cv2.CAP_PROP_FPS)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        return {
            "width": width,
            "height": height,
            "fps": fps,
            "frame_count": frame_count,
            "duration": frame_count / fps if fps > 0 else None
        }
    finally:
        capture.release()
