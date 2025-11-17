class User:
    """用户信息"""
    user_name = 'xiaoming'
    age = 10

    def __init__(self):
        pass


## read
print("--------读类变量---------------")
print(f"user name:{User.user_name}")
print(f"user age:{User.age}")

print("--------更新类变量---------------")
## update
User.user_name = 'xiaoli'
User.age = 20
print("--------读类变量---------------")
print(f"user name: {User.user_name}")
print(f"user age: {User.age}")

## 实例 访问  类 变量

print("--------读实例变量---------------")
user = User()
## 实例变量 不会影响类变量，类变量会影响实例变量
print(f"user name: {user.user_name}")
print(f"user age: {user.age}")
print("--------更新实例变量---------------")
user.age = 30
print(f"user name: {user.user_name}")
print(f"user age: {user.age}")

## 类变量
print("--------读类变量---------------")
print(f"user name: {User.user_name}")
print(f"user age: {User.age}")
