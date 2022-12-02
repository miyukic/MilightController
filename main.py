#!/usr/bin/python3
# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# ダブルShift を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

import socket
import time


def print_hi(name):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


class LightController:

    def __init__(self, ipaddr='192.168.1.255', port=8899, group=0):
        self._IPADDR    = ipaddr
        self._PORT      = port
        self._GROUP     = group # 0~3

    def light_increase(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect((self._IPADDR, self._PORT))
            cmd = [0x45, 0x00]
            cmd[0] += self._GROUP * 2
            sock.send(bytes(cmd))

    def light_reduce(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect((self._IPADDR, self._PORT))
            cmd = [0x4e, 0xaa]
            cmd[0] += self._GROUP * 2
            sock.send(bytes(cmd))

    def light_off(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect((self._IPADDR, self._PORT))
            cmd = [0x46, 0x00]
            cmd[0] += self._GROUP * 2
            sock.send(bytes(cmd))

    def light_on(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect((self._IPADDR, self._PORT))
            cmd = [0x45, 0x00]
            cmd[0] += self._GROUP * 2
            sock.send(bytes(cmd))


def main():
    lc = LightController(group=1)
    lc.light_off()
    lc.light_on()
    flag = True
    fps = 5
    while True:
        time.sleep(1 / fps)
        if flag:
            lc.light_off()
            flag = False
        else:
            lc.light_on()
            flag = True


if __name__ == '__main__':
    main()
#    print_hi('PyCharm')
