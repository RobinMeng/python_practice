import os
import uuid
from pathlib import Path


def len_byte_file(path):
    """
    读取文件bytes length
    """
    path = os.path.abspath(os.path.expanduser(path))
    return os.path.getsize(path)


def read_byte_file(path):
    """
    读取文件bytes
    """
    path = os.path.abspath(os.path.expanduser(path))
    return Path(path).expanduser().resolve().read_bytes()


def write_random_file(folder_path, _bytes):
    file_name = str(uuid.uuid4()) + ".txt"
    path = os.path.abspath(os.path.expanduser(folder_path)) + "/" + file_name
    print(path)
    try:
        with open(path, mode="wb") as file:
            file.write(_bytes)
            file.flush()
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    write_random_file()
