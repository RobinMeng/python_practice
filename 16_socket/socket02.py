## 短连接客户端:
import socket

host = "127.0.0.1"
port = 8000


def client():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with s:
            s.connect((host, port))
            msg = input("发些信息给服务端吧 (q退出): ").strip()
            if msg.lower() == 'q':
                break
            s.sendall(msg.encode(encoding="utf-8"))
            data = s.recv(2048)
            print(f"服务端消息: {data.decode()}")


if __name__ == '__main__':
    client()
