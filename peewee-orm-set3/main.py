from models import *

db.connect()

fruit1 = Fruit(fruit_name='Orange', amount=220, country='Morocco')
fruit1.save()
fruit2 = Fruit(fruit_name='Banana', amount=400, country='Algeria')
fruit2.save()

db.close()
