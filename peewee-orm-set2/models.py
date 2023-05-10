import sqlite3
from peewee import *

conn = sqlite3.connect('my_database.db')
conn.close()
db = SqliteDatabase('my_database.db')


class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db