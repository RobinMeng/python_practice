## socket 文件传输 client

import socket
import struct
from utils import file_util as futil
import socket05 as punti

ip = "127.0.0.1"
port = 8000


def client():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(type(sock))
        sock.connect((ip, port))
        with sock:
            while True:
                try:
                    msg = input("发些信息给服务端吧 (q退出): ").strip()
                    if not msg:
                        continue
                    sock.sendall(punti.package_msg_string(msg))

                    header = sock.recv(4)
                    if not header:
                        break
                    length = struct.unpack("!I", header)[0]
                    data = sock.recv(length)
                    if not data:
                        break
                    body = data.decode(encoding="utf-8")
                    print(f"服务端数据:{body}")

                    if "bye" == body:
                        break

                    if "text.txt" == body:
                        file_header = sock.recv(4)
                        if not file_header:
                            break
                        file_length = struct.unpack("!I", file_header)[0]
                        file_data = sock.recv(file_length)
                        futil.write_random_file("./files", file_data)
                        print("客户端接受文件写入成功~~")
                        break
                except Exception as ex:
                    print(ex)
                    break


if __name__ == '__main__':
    client()
