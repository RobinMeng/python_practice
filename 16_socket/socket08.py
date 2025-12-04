## socket 文件传输 server
from utils import file_util as futil
import socket
import socket05 as sutil
import struct

ip = "127.0.0.1"
port = 8000


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(10)
    with s:
        while True:
            print("服务端等待连接")
            sock, addr = s.accept()
            print("服务端等待连接成功")
            with sock:
                while True:
                    """
                        保持服务端长连接
                    """
                    try:
                        header = sock.recv(4)
                        if not header:
                            ## 连接断开
                            break
                        length = struct.unpack("!I", header)[0]
                        data = sock.recv(length)
                        if not data:
                            break
                        body_msg = data.decode(encoding="utf-8")

                        if "bye" == body_msg:
                            ## 断开连接
                            sock.sendall(sutil.package_msg_string("bye"))
                            break
                        if "text.txt" == body_msg:
                            ## 发送文件只客户端
                            sock.sendall(sutil.package_msg_string("text.txt"))
                            sock.sendall(sutil.package_bytes(futil.read_byte_file("./files/file.txt")))

                        print("客户端消息", body_msg)
                        sock.sendall(sutil.package_msg_string("done!"))

                    except Exception as ex:
                        print(ex)


if __name__ == '__main__':
    server()
