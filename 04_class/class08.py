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
## 变量属性
print(dir(user))
## 判断是否包含某个属性
print(hasattr(user, 'aaa'))
print(hasattr(user, 'name'))
