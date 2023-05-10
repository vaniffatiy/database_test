from models import *

db.connect()
db.create_tables([User])
db.close()
