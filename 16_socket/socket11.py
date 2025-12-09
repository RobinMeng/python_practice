## 广播 server

import socket
import threading

ip = ""
port = 8000


def server():
    threading.Thread(target=tpc_server).start()
    threading.Thread(target=udp_server).start()


def tpc_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    with s:
        while True:
            print("\ntcp 等待客户端连接")
            sock, addr = s.accept()
            print("\ntcp 客户端连接成功")
            with sock:
                while True:
                    try:
                        body = sock.recv(1024)
                        if not body:
                            break
                        print(f"tcp:msg:{body.decode(encoding='utf-8')}")
                        sock.sendall(str(addr).encode(encoding="utf-8"))
                    except Exception as ex:
                        print(ex)
                        break


def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    with sock:
        while True:
            try:
                print("\nudp 等待接收客户端信息")
                body = sock.recvfrom(1024)
                print(f"udp:msg{body}")
            except Exception as ex:
                print(ex)


if __name__ == '__main__':
    server()
