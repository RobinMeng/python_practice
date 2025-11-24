## 使用sqlite
from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('./db/my_database.db')


## 定义模型
class User(Model):
    class Meta:
        database = db

    username = CharField(unique=True)
    age = IntegerField()


if __name__ == "__main__":
    db.connect()
    db.create_tables([User])
    user = User(username="Harry", age=23)
    get_user = User.get(User.username == "Harry")
    print(f"name: {get_user.username}, age: {get_user.age}")
    users = User.select().where((User.age > 20)).execute()
    for u in users:
        print(u)
