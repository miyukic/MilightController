#!/usr/bin/python3
# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# ダブルShift を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

import socket

def print_hi(name):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。

def main():
    IPADDR = '192.168.1.255'
    PORT = 8899
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((IPADDR, PORT))
        cmd = [0x47, 0x00]
        sock.send(bytes(cmd))
    #sock.send("hello".encode("utf-8"))

    #cmd = [ 0x31, 0x00, 0x00, 0x08, 0x04, 0x01, 0x00, 0x00, 0x00, zone ]

    #ctrlData = [ 0x80, 0x00, 0x00, 0x00, 0x11,
    #            sessionId1,  sessionId2, 0x00, iboxSeq, 0x00,
    #            cmd[0], cmd[1], cmd[2], cmd[3], cmd[4],
    #            cmd[5], cmd[6], cmd[7], cmd[8], cmd[9],
    #            0x00, checkSum ]

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    main()
#    print_hi('PyCharm')
