# main.py

import cv2
import time
from video_capture import VideoCapture
from hand_detection import HandDetector
from gesture_recognition import GestureRecognizer
from command_sender import CommandSender

def main():
    # 初始化各个模块
    video = VideoCapture()
    detector = HandDetector()
    sender = CommandSender()
    recognizer = GestureRecognizer(video.width, video.height)

    prev_time = 0
    while True:
        # 读取一帧视频
        frame = video.read_frame()
        if frame is None:
            continue

        # 检测手部，并绘制所有手部特征
        image, results = detector.find_hands(frame, draw=True)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 获取关键点位置和边界框
                landmark_positions, bbox = recognizer.get_landmark_positions(hand_landmarks)

                # 识别手势
                gesture_info = recognizer.recognize_gesture(landmark_positions)

                # 发送命令（限制发送频率）
                current_time = time.time()
                if current_time - prev_time > 0.1:  # 每 0.1 秒发送一次
                    sender.send_command(gesture_info)
                    prev_time = current_time

                # 可视化特定手势（可选）
                positions = gesture_info['positions']
                thumb_tip = positions[4]
                index_finger_tip = positions[8]
                cv2.circle(image, thumb_tip, 10, (255, 0, 255), -1)
                cv2.circle(image, index_finger_tip, 10, (255, 0, 255), -1)
                cv2.line(image, thumb_tip, index_finger_tip, (255, 0, 255), 5)

                # 绘制绿色边界框
                x_min, y_min, x_max, y_max = bbox
                cv2.rectangle(image, (x_min - 30, y_min - 30), (x_max + 30, y_max + 30), (0, 255, 0), 2)

        else:
            # 如果没有检测到手部，翻转图像以保持一致性
            image = cv2.flip(frame, 1)

        # 显示图像
        cv2.imshow('Virtual Drag and Drop', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    video.release()
    detector.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
