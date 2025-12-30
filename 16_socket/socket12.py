## 回声服务器
import socket
import select
import struct

ip = "127.0.0.1"
port = 8000

rList = []
wList = []
xList = []


def socket_server():
    sock_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock_server.bind((ip, port))
    sock_server.listen(10)
    sock_server.setblocking(False)
    rList.append(sock_server)
    print("echo server running....")
    print("watting a connect...")
    while True:
        rlist, wrlist, xlist = select.select(rList, wList, xList)
        for rdata in rlist:
            if rdata is sock_server:
                c_sock, addr = sock_server.accept()
                c_sock.setblocking(False)
                rList.append(c_sock)
                print(f"new connect:{c_sock}")
            else:
                c_sock: socket.socket = rdata
                length_msg = c_sock.recv(4)
                if not length_msg:
                    rList.remove(c_sock)
                length = struct.unpack("!I", length_msg[:4])[0]
                data_msg = recv_exact(c_sock, length)
                print(f"msg:{c_sock}-{data_msg.decode(encoding='utf-8')}")
                c_sock.sendall(struct.pack("!I", length) + data_msg)


def recv_exact(sock, n):
    """精确收 n 字节，不足就循环，返回 bytes 或 None（对端关闭）"""
    buf = bytearray()
    while len(buf) < n:
        try:
            data = sock.recv(n - len(buf))
        except BlockingIOError:  # 非阻塞模式下缓冲区空
            continue
        if not data:  # 对端关闭
            return None
        buf.extend(data)
    return bytes(buf)


if __name__ == '__main__':
    socket_server()
