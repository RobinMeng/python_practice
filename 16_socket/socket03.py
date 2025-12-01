## 长连接 服务端
import socket

ip = "127.0.0.1"
port = 8000


def keep_alive_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with s:
        s.bind((ip, port))
        s.listen(10)
        while True:
            print("等待连接中")
            sock, addr = s.accept()
            print(f"连接成功:{addr}")
            with sock:
                while True:
                    try:
                        data = sock.recv(1024)
                        if not data:
                            break
                        msg = data.decode().strip()
                        if not msg:
                            continue

                        print(f"client msg:{msg}")
                        if "q" == msg.lower():
                            sock.sendall("bye".encode(encoding="utf-8"))
                            break
                        else:
                            sock.sendall(str(addr).encode(encoding="utf-8"))
                    except Exception as ex:
                        print(ex)
                        break


if __name__ == '__main__':
    keep_alive_server()
