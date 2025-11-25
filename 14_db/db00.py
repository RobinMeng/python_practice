from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('./db/my_database.db')


class BaseModel(Model):
    class Meta:
        database = db
