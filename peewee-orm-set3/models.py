import sqlite3
from peewee import *

conn = sqlite3.connect('my_database.db')
conn.close()
db = SqliteDatabase('my_database.db')


class Fruit(Model):
    fruit_name = CharField()
    country = CharField()
    amount = IntegerField()

    class Meta:
        database = db