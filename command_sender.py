# command_sender.py

import requests
import threading
from config import IP_ADDR

class CommandSender:
    def __init__(self, ip_addr=IP_ADDR):
        self.ip_addr = ip_addr

    def send_command(self, gesture_info):
        # 构建命令
        command = self.construct_command(gesture_info)
        url = "http://" + self.ip_addr + "/js?json=" + command

        # 使用线程异步发送请求
        thread = threading.Thread(target=self.async_get, args=(url,))
        thread.start()

    def construct_command(self, gesture_info):
        hand_size = gesture_info['hand_size']
        thumb_index_distance = gesture_info['thumb_index_distance']
        positions = gesture_info['positions']
        root_tip_x, root_tip_y = positions[0]

        command = (
            '{"T":1041,"x":' + str(40 + (hand_size / 100) * 300) +
            ',"y":' + str(448 - root_tip_x * 1.4) +
            ',"z":' + str(470 - root_tip_y * 1.2) +
            ',"t":' + str(3.24 - (thumb_index_distance / hand_size) * 0.75) + '}'
        )
        return command

    def async_get(self, url):
        try:
            requests.get(url, timeout=0.1)
        except requests.exceptions.RequestException as e:
            print(f"请求出错：{e}")
