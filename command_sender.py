# command_sender.py

import requests
from config import IP_ADDR


class CommandSender:
    def __init__(self, ip_addr=IP_ADDR):
        self.ip_addr = ip_addr

    def send_command(self, gesture_info):
        hand_size = gesture_info['hand_size']
        thumb_index_distance = gesture_info['thumb_index_distance']
        positions = gesture_info['positions']
        root_tip_x, root_tip_y = positions[0]

        # 构建命令
        command = (
            '{"T":1041,"x":' + str(40 + (hand_size / 100) * 300) +
            ',"y":' + str(448 - root_tip_x * 1.4) +
            ',"z":' + str(470 - root_tip_y * 1.2) +
            ',"t":' + str(3.24 - (thumb_index_distance / hand_size) * 0.75) + '}'
        )
        url = "http://" + self.ip_addr + "/js?json=" + command

        # 发送请求
        try:
            requests.get(url)
        except requests.exceptions.RequestException as e:
            print(f"请求出错：{e}")
