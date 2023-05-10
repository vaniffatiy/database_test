from models import *

db.connect()

user = User(name='John', email='john@example.com', password='password')
user.save()

db.close()
