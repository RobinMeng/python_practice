## 客户端广播
import socket

ip = "127.0.0.1"
port = 8000


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    pass


if __name__ == '__main__':
    client()
