import socket

ip = "127.0.0.1"
port = 8000


def socket_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("connect success...")
    while True:
        msg = input("please send msg!!!\n")
        sock.send(msg.encode(encoding="utf-8"))
        echo_msg = sock.recv(1024)
        print(f"echo server msgs:{echo_msg.decode(encoding='utf-8')}")


if __name__ == '__main__':
    socket_client()
