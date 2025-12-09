## 客户端广播
import socket

ip = "127.0.0.1"
port = 8000
board_cast = "<broadcast>"


def client():
    tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sock.connect((ip, port))

    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        body = input("请输入格式 tcp/upd:msg\n")
        switch_client = body.split(":")[0]
        body = body.split(":")[1]
        try:
            if "tcp" == switch_client:
                tcp_sock.sendall(body.encode(encoding="utf-8"))
                recv_body = tcp_sock.recv(1024)
                print(recv_body.decode(encoding="utf-8"))
            if "udp" == switch_client:
                udp_sock.sendto(body.encode(encoding="utf-8"), (board_cast, port))
                print("udp 消息发送成功")
        except Exception as ex:
            print(ex)


def udp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.connect((ip, port))
    return sock


def tcp_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    return sock


def init():
    tcp_sock = tcp_client()
    udp_sock = udp_client()


if __name__ == '__main__':
    init()
    client()
