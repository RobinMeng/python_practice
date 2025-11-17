## 方法
class User:
    def __init__(self):
        pass

    ## 对象方法
    def say(self):
        """对象方法从对象中调用"""
        print("hello world")

    @classmethod
    def sayNext(cls):
        """类方法无需实例即可调用,允许访问类变量，无法访问实例变量"""
        print("hello next")

    @staticmethod
    def sayLast():
        """静态方法与类方法一样，无需实例即可访问方法，不可以访问类变量，也不可以访问实例变量"""
        print("hello last")


## 实例 即可以调用 实例方法，也可以访问 ，类方法 还可以访问 静态方法
user = User()
user.say()
user.sayNext()
user.sayLast()

## 类可以访问 类方法 和 静态方法
User.sayNext()
User.sayLast()
