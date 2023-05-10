# from peewee import *
import psycopg2

# conn = PostgresqlDatabase('my_database2', user='postgres', password='mypassword',
#                         host='localhost', port=5432)
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase2",
    user="postgres",
    password="mypassword",
    port="5432"
)
cursor = conn.cursor()

# class BaseModel(Model):
#     class Meta:
#         database = conn
#
#
# class Fruit(BaseModel):
#     fruit_id = AutoField(column_name='ID')
#     fruit_name = TextField(column_name='Fruit', null=True)
#
#     class Meta:
#         table_name = 'Fruit'

class Fruit:
    def __init__(self, fruit_id, fruit_name):
        self.fruit_id = fruit_id
        self.fruit_name = fruit_name


def print_last_three_fruits():
    print('########################################################')
    for fruit_id, fruit_name in cursor.fetchall():
        fruit = Fruit(fruit_id, fruit_name)
        print('fruit: ', fruit.fruit_id, fruit.fruit_name)


cursor.execute("SELECT Fruit, ID FROM Fruit ORDER BY Fruit LIMIT 3")
results = cursor.fetchall()
print(results)


cursor.execute("SELECT ID, Fruit FROM Fruit WHERE ID = 1")
fruit_data = cursor.fetchone()
fruit = Fruit(fruit_data[0], fruit_data[1])
print('fruit: ', fruit.fruit_id, fruit.fruit_name)


# query = Fruit.select()
# print(query) #общий запрос - но лучше уточнить, как ниже

cursor.execute("SELECT ID, Fruit FROM Fruit WHERE ID < 10 ORDER BY ID DESC LIMIT 5")
fruits_selected = cursor.fetchall()
for fruit_data in fruits_selected:
    fruit = Fruit(fruit_data[0], fruit_data[1])
    print('fruit: ', fruit.fruit_id, fruit.fruit_name)



cursor.execute("INSERT INTO Fruit (fruit_id) VALUES ('Pineapple')")
conn.commit()



cursor.execute("INSERT INTO Fruit (Fruit) VALUES ('Cherry') RETURNING ID")
fruit_id = cursor.fetchone()[0]
conn.commit()


fruits_data = [{'Fruit': 'Peach'}, {'Fruit': 'Pear'}]
for fruit_data in fruits_data:
    cursor.execute("INSERT INTO Fruit (Fruit) VALUES (%(fruit_name)s)", fruit_data)
conn.commit()


print_last_three_fruits()


cursor.execute("UPDATE Fruit SET fruit_name = 'Good Peach!' WHERE ID = 15")
conn.commit()

print_last_three_fruits()


cursor.execute("UPDATE Fruit SET Fruit = CONCAT(Fruit, '!!!') WHERE ID > 15")
conn.commit()

print_last_three_fruits()

cursor.execute("DELETE FROM Fruit WHERE ID = 17")
conn.commit()

print_last_three_fruits()

cursor.execute("DELETE FROM Fruit WHERE ID > 15")
conn.commit()

print_last_three_fruits()

conn.close()
