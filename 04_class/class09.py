## 对象信息字符串
class User:
    def __init__(self):
        self.name = 'xiaoming'
        self.age = 20
        pass

    def __str__(self):
        return f"用户名:{self.name},年龄:{self.age}"

    def __repr__(self):
        return str({"name": self.name, "agg": self.age})


user = User()
## 对象类型
print(type(user))
## 判断是否是 class 的实例
print(isinstance(user, User))
