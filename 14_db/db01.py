## 使用sqlite
from peewee import CharField, IntegerField
from db00 import BaseModel


## 定义模型
class User(BaseModel):
    id = IntegerField(unique=True)
    username = CharField()
    age = IntegerField()


##  创建表
def create_table():
    User.create_table()


## 保存数据
def save_data():
    User.create(id=1, username='test1', age=3)


## 保存数据
def save_data_2():
    user = User(id=2, username='test2', age=4)
    user.save()


## 保存数据
def save_data_3():
    User.insert(id=3, username='test3', age=4).execute()


## 查询数据
def query_data():
    data = User.get(id=1)
    print(type(data))
    print(data.__dict__)


## 查询数据
def query_data2():
    list_user = User.select()
    for user in list_user:
        print(user.__dict__)


## 查询数据
def query_data3():
    list_user = User.select().where(User.id == 1).execute()
    for user in list_user:
        print(user.__dict__)


## 更新数据
def update_data():
    User.update(age=40).where(User.id == 1).execute()


## 删除数据
def del_data():
    User.delete().where(User.id == 1).execute()


## 排序
def order_data():
    list_data = User.select().order_by(User.age.desc()).execute()
    print("*" * 50)
    for user in list_data:
        print(user.__dict__)


if __name__ == "__main__":
    # create_table()
    # save_data()
    # save_data_2()
    # save_data_3()
    # update_data()
    # query_data()
    # query_data2()
    # del_data()
    query_data2()
    query_data()
    query_data2()
    order_data()

"""
peewee语法
模型类.操作动作[.条件][.修饰][.execute()]

操作动作
select() - 查询
insert() - 插入
update() - 更新
delete() - 删除
create() - 创建实例并保存（快捷方式）
get() - 获取单条记录

条件
where() - 条件过滤
orwhere() - OR 条件

修饰
order_by() - 排序
limit() - 限制数量
offset() - 偏移量
join() - 关联查询

执行
execute() - 显式执行


"""