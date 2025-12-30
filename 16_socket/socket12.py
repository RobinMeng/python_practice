## 回声服务器
import socket
import select

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
                msg = c_sock.recv(1024)
                if not msg:
                    rList.remove(c_sock)
                print(f"msg:{c_sock}-{msg.decode(encoding='utf-8')}")
                c_sock.sendall(msg)


if __name__ == '__main__':
    socket_server()
