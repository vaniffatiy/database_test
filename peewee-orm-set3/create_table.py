from models import *

db.connect()
db.create_tables([Fruit])
db.close()
