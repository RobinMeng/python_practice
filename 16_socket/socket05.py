## 文本二进制打包解包
import struct


def package_msg_string(msg):
    if not msg:
        return None
    length = len(msg)
    length_bytes = struct.pack('!I', length)
    packed_data = length_bytes + msg.encode('utf-8')
    return packed_data


def unpackage_msg_string(msg):
    if not msg:
        return None
    length = struct.unpack('!I', msg[:4])[0]
    string_data = msg[4:4 + length].decode('utf-8')
    return string_data


if __name__ == '__main__':
    data = package_msg_string("hello world")
    print(type(data))
    print(data)
    print(unpackage_msg_string(data))
