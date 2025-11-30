##  短连接服务端
import socket

host = "127.0.0.1"
port = 8000


def server():
    ## ipv4 字节流
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with s:
        try:
            s.bind((host, port))
            s.listen(10)
            while True:
                print(" 服务端 等待连接 ...")
                conn, addr = s.accept()
                print(f"服务端 连接成功 ...{addr}")
                with conn:
                    print(f"ip:{conn.getpeername()}")
                    msg = conn.recv(2048)
                    print(f"f msg:{msg}")
                    reply = f"{conn.getpeername()}".encode()
                    conn.sendall(reply)
        except BaseException as be:
            print(be)


if __name__ == '__main__':
    server()
