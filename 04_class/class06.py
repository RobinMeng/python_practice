## 私有变量 和 私有方法
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __say(self):
        print(f"user name: {self.__name}")
        print(f"user age: {self.__age}")


user = User('xxx', 12)
##  exception
##print(user.__name)
##user.__say()
