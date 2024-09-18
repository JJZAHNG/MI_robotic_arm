# video_capture.py

import cv2
from config import CAMERA_INDEX


class VideoCapture:
    def __init__(self, camera_index=CAMERA_INDEX):
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def read_frame(self):
        success, frame = self.cap.read()
        if not success:
            print("无法获取帧！")
            return None
        frame = cv2.resize(frame, (self.width, self.height))
        return frame

    def release(self):
        self.cap.release()
