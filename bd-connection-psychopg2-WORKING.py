# docker run --name mydatabase2 -e POSTGRES_PASSWORD=mypassword -d postgres
# docker exec -it mydatabase2 psql -U postgres -c "create database mydatabase2

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase2",
    user="postgres",
    password="mypassword",
    port="5432"
)

cur = conn.cursor()

cur.execute("CREATE TABLE Fruit_Basket (id serial PRIMARY KEY, data varchar, num integer);")
cur.execute("INSERT INTO Fruit_Basket (data, num) VALUES (%s, %s)", ("Banana", 220))
cur.execute("INSERT INTO Fruit_Basket (data, num) VALUES (%s, %s)", ("Apple", 400))
# cur.execute("DELETE FROM Fruit_Basket WHERE data = 'Apple' AND num = 400")
# cur.execute("DELETE FROM Fruit_Basket WHERE data = 'Banana' AND num = 220")


conn.commit()

cur.execute("SELECT * FROM Fruit_Basket;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
