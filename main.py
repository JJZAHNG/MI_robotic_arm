# main.py

import cv2
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

    while True:
        # 读取一帧视频
        frame = video.read_frame()
        if frame is None:
            continue

        # 检测手部
        results = detector.find_hands(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 获取关键点位置
                landmark_positions = recognizer.get_landmark_positions(hand_landmarks)

                # 识别手势
                gesture_info = recognizer.recognize_gesture(landmark_positions)

                # 发送命令
                sender.send_command(gesture_info)

                # 可视化
                positions = gesture_info['positions']
                thumb_tip = positions[4]
                index_finger_tip = positions[8]
                cv2.circle(frame, thumb_tip, 10, (255, 0, 255), -1)
                cv2.circle(frame, index_finger_tip, 10, (255, 0, 255), -1)
                cv2.line(frame, thumb_tip, index_finger_tip, (255, 0, 255), 5)

        # 显示图像
        preview_size_scale = 1.8
        img_preview = cv2.resize(
            frame,
            (int(frame.shape[1] * preview_size_scale), int(frame.shape[0] * preview_size_scale))
        )
        cv2.imshow('Virtual Drag and Drop', img_preview)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    video.release()
    detector.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
