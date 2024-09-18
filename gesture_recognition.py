# gesture_recognition.py

import math


class GestureRecognizer:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_landmark_positions(self, hand_landmarks):
        landmark_positions = {}
        for idx, lm in enumerate(hand_landmarks.landmark):
            x, y = int(lm.x * self.width), int(lm.y * self.height)
            landmark_positions[idx] = (x, y)
        return landmark_positions

    def recognize_gesture(self, landmark_positions):
        # 计算手势，例如判断拇指和食指之间的距离
        thumb_tip = landmark_positions[4]    # 拇指指尖
        index_finger_tip = landmark_positions[8]  # 食指指尖

        # 计算距离
        distance = math.hypot(
            thumb_tip[0] - index_finger_tip[0],
            thumb_tip[1] - index_finger_tip[1]
        )

        # 计算手的尺寸，用于归一化
        wrist = landmark_positions[0]
        middle_finger_tip = landmark_positions[12]
        hand_size = math.hypot(
            middle_finger_tip[0] - wrist[0],
            middle_finger_tip[1] - wrist[1]
        )

        # 返回计算结果
        return {
            'thumb_index_distance': distance,
            'hand_size': hand_size,
            'positions': landmark_positions
        }
