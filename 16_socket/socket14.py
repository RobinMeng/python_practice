## 回声服务器 socket selector
import selectors
import socket
import struct

ip = "127.0.0.1"
port = 8000

selector = selectors.DefaultSelector()


def server():
    srv_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    srv_sock.bind((ip, port))
    srv_sock.listen(10)
    srv_sock.setblocking(False)
    selector.register(srv_sock, selectors.EVENT_READ, srv_accept)


def srv_accept(srv_sock: socket.socket):
    print("waitting connectting ...")
    clt_sock, addr = srv_sock.accept()
    print(f"connect successful clt_sock:{clt_sock},addr:{addr}")
    clt_sock.setblocking(False)
    selector.register(clt_sock, selectors.EVENT_READ, srv_read)


def srv_read(clt_sock: socket.socket):
    data_length = recv_exact(clt_sock, 4)
    if not data_length:
        return
    msg_len = struct.unpack("!I", data_length)[0]
    data_msg = recv_exact(clt_sock, msg_len)
    if not data_msg:
        return
    print(f"clt_sock:msg:{data_msg.decode(encoding='utf-8')}")
    clt_sock.send(struct.pack("!I", msg_len) + data_msg)


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
    server()
    print('server running ...')
    try:
        while True:
            for key, _ in selector.select():
                call_back = key.data
                print(f"selector key:{key}")
                call_back(key.fileobj)
    except BaseException as ex:
        print(ex)
