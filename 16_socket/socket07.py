## 封包数据的客户端
import socket05 as putils
import socket
import struct

ip = "127.0.0.1"
port = 8000


def client():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print("新的连接连接成功～～")
        with s:
            while True:
                try:
                    msg = input("发些信息给服务端吧 (q退出): ").strip()
                    if not msg:
                        continue
                    s.sendall(putils.package_msg_string(msg))
                    header = s.recv(4)
                    length = struct.unpack("!I", header)[0]
                    data = s.recv(length)
                    print(f"服务单返回信息:{data.decode(encoding='utf-8')}")
                    if "bye~" == data.decode(encoding='utf-8'):
                        break
                except Exception as ex:
                    print("error client {}", ex)
                    break


if __name__ == '__main__':
    client()
