## 封包数据的服务端
import socket
import struct
import socket05 as puntil

ip = "127.0.0.1"
port = 8000


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    with s:
        while True:
            print("等待连接中")
            sock, addr = s.accept()
            print(f"连接成功,客户端地址:{addr}")
            with sock:
                while True:
                    try:
                        header = sock.recv(4)
                        if not header:
                            break
                        ## length
                        length = struct.unpack('!I', header[:4])[0]
                        data = sock.recv(length)
                        if not data:
                            continue
                        ## body
                        body = data.decode(encoding="utf-8")
                        if "q" == body:
                            sock.sendall(puntil.package_msg_string(str('bye~')))
                            break
                        print(f"收到客户端信息:{body}")
                        sock.sendall(puntil.package_msg_string(str(addr)))
                    except Exception as ex:
                        print("error server:{}", ex)
                        break


if __name__ == '__main__':
    server()
