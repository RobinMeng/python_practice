## 长连接client
import socket

ip = "127.0.0.1"
port = 8000


def keep_alive_client():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        with s:
            while True:
                try:
                    msg = input("发些信息给服务端吧 (q退出): ").strip()
                    if not msg:
                        continue
                    s.sendall(msg.encode(encoding="utf-8"))
                    data = s.recv(2048)
                    print(f"服务端消息: {data.decode()}")
                    if "q" == msg.lower():
                        break
                except Exception as ex:
                    print(ex)
                    break


if __name__ == '__main__':
    keep_alive_client()
