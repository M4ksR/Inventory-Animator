import cv2

def count_video_frames(video_path, max_frames):
    capture = cv2.VideoCapture(video_path)

    try:
        if not capture.isOpened():
            raise ValueError("Не удалось открыть видео")

        count = 0
        while count < max_frames and capture.grab():
            count += 1

        return count

    finally:
        capture.release()

def get_video_metadata(path):
    capture = cv2.VideoCapture(path)
    try:
        if not capture.isOpened():
            raise ValueError("Не удалось открыть видео")

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
