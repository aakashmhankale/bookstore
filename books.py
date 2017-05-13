import psycopg2
def create_table():
    connection=psycopg2.connect("dbname='database1' user='postgres' password='lifeisgood123' host='localhost' port='5432'")
    cur=connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (Item TEXT, Quantity INTEGER, Price REAL)")
    connection.commit()
    connection.close()

def insert(Item,Quantity,Price):
    connection=psycopg2.connect("dbname='database1' user='postgres' password='lifeisgood123' host='localhost' port='5432'")
    cur=connection.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(Item,Quantity,Price))
    connection.commit()
    connection.close()

def view():
    connection=psycopg2.connect("dbname='database1' user='postgres' password='lifeisgood123' host='localhost' port='5432'")
    cur=connection.cursor()
    cur.execute("SELECT * from store")
    rows=cur.fetchall()
    connection.close()
    return rows

def delete(Item):
    connection=psycopg2.connect("dbname='database1' user='postgres' password='lifeisgood123' host='localhost' port='5432'")
    cur=connection.cursor()
    cur.execute("DELETE FROM store WHERE Item=%s",(Item,))
    connection.commit()
    connection.close()

def update(Quantity,Price,Item):
    connection=psycopg2.connect("dbname='database1' user='postgres' password='lifeisgood123' host='localhost' port='5432'")
    cur=connection.cursor()
    cur.execute("UPDATE store SET Quantity=%s,Price=%s WHERE Item=%s",(Quantity,Price,Item))
    connection.commit()
    connection.close()

create_table()
insert('Apple',10,100)
insert('Mango',20,200)
insert('Strawberry',60,600)
update(50,500,'Mango')
print(view())
#update(1,100,"Water Glass")
#delete("Wine Glass")
#print(view())
