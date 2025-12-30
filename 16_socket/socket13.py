import socket
import struct

ip = "127.0.0.1"
port = 8000


def socket_client():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("connect success...")
    with sock:
        while True:
            msg = input("please send msg!!!\n")
            length = len(msg)
            print(f"length:{length}")
            if 0 == length:
                continue
            sock.send(struct.pack("!I", length) + msg.encode(encoding="utf-8"))
            echo_msg_length = sock.recv(4)
            recv_len = struct.unpack("!I", echo_msg_length[:4])[0]
            echo_msg = recv_exact(sock, recv_len)
            if not echo_msg:
                break
            print(f"echo server msgs:{echo_msg.decode(encoding='utf-8')}")


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
    socket_client()
