## 回声服务器 socket selector read write
import selectors
import socket
import struct
import traceback

ip = "127.0.0.1"
port = 8000
out_bufs = {}
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
    out_bufs[clt_sock] = bytearray()
    selector.register(clt_sock, selectors.EVENT_READ, srv_read)


def srv_read(clt_sock: socket.socket):
    data_length = recv_exact(clt_sock, 4)
    if not data_length:
        return
    msg_len = struct.unpack("!I", data_length)[0]
    data_msg = recv_exact(clt_sock, msg_len)
    if not data_msg:
        return
    write_buff: bytearray = out_bufs[clt_sock]
    write_buff.extend(data_length + data_msg)
    ##print(f"clt_sock:msg:{data_msg.decode(encoding='utf-8', errors='replace')}")
    if len(write_buff) > 0:
        print(f"clt_sock: read msg successfull write event open()")
        selector.modify(fileobj=clt_sock, events=selectors.EVENT_READ | selectors.EVENT_WRITE,
                        data=(srv_read, srv_write))


def srv_write(clt_sock: socket.socket):
    print("srv_write")
    if not out_bufs[clt_sock]:
        selector.modify(fileobj=clt_sock, events=selectors.EVENT_READ, data=srv_read)
        return
    write_buff: bytearray = out_bufs[clt_sock]
    count = clt_sock.send(write_buff)
    del out_bufs[clt_sock][:count]
    print(f"clt_sock: write msg successfull count is :{count}")
    if 0 == len(out_bufs[clt_sock]):
        selector.modify(fileobj=clt_sock, events=selectors.EVENT_READ, data=srv_read)
        print(f"clt_sock: write msg successfull write event close()")


def recv_exact(sock, n):
    """精确收 n 字节，不足就循环，返回 bytes 或 None（对端关闭）"""
    buf = bytearray()
    while len(buf) < n:
        try:
            data = sock.recv(n - len(buf))
        except BlockingIOError:  # 非阻塞模式下缓冲区空
            return None
        if not data:  # 对端关闭
            return None
        buf.extend(data)
    return bytes(buf)


if __name__ == '__main__':
    server()
    print('server running ...')
    try:
        while True:
            for key, mask in selector.select():
                if key.fd == -1:
                    continue
                if key.data is srv_accept:
                    srv_accept(key.fileobj)
                    continue
                if mask & selectors.EVENT_READ:
                    srv_read(key.fileobj)
                    continue
                if mask & selectors.EVENT_WRITE:
                    srv_write(key.fileobj)

    except BaseException as ex:
        print(ex)
        traceback.print_tb(ex.__traceback__)
