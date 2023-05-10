from peewee import *

conn = PostgresqlDatabase('my_database2', user='postgres', password='mypassword',
                        host='localhost', port=5432)
# conn = PostgresqlDatabase('Chinook_PostgreSql.sql')


class BaseModel(Model):
    class Meta:
        database = conn


class Fruit(BaseModel):
    fruit_id = AutoField(column_name='ID')
    fruit_name = TextField(column_name='Fruit', null=True)

    class Meta:
        table_name = 'Fruit'


def print_last_three_fruits():
    print('########################################################')
    cur_query = Fruit.select().limit(5).order_by(Fruit.fruit_id.desc())
    for item in cur_query.dicts().execute():
        print('fruit: ', item)


cursor = conn.cursor()
cursor.execute("SELECT Fruit FROM Fruit ORDER BY Fruit LIMIT 3")
results = cursor.fetchall()
print(results)


fruit = Fruit.get(Fruit.artist_id == 1)
print('fruit: ', fruit.fruitt_id, fruit.name)

# query = Fruit.select()
# print(query) #общий запрос - но лучше уточнить, как ниже

query = Fruit.select().where(Fruit.fruit_id < 10).\
                        limit(5).order_by(Fruit.fruit_id.desc())
print(query)


fruits_selected = query.dicts().execute()
print(fruits_selected) #выдает в ответе итератор, поэтому ниже используем цикл

for artist in fruits_selected:
    print('fruit: ', fruit)


Fruit.create(name='Pineapple')

fruit = Fruit(name='Cherry')
fruit.save()

fruits_data = [{'name': 'Peach'}, {'name': 'Pear'}]
Fruit.insert_many(fruits_data).execute()


print_last_three_fruits()


fruit = Fruit(name='Good Peach!')
fruit.fruit_id = 15
fruit.save()

print_last_three_fruits()


query = Fruit.update(name=Fruit.name + '!!!').where(Fruit.fruit_id > 15)
query.execute()

print_last_three_fruits()


fruit = Fruit.get(Fruit.artist_id == 279)
fruit.delete_instance()

print_last_three_fruits()

query = Fruit.delete().where(Fruit.fruit_id > 15)
query.execute()

print_last_three_fruits()

conn.close()
