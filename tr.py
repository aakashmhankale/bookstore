import sqlite3
def create_table():
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (Item TEXT, Quantity INTEGER, Price REAL)")
    connection.commit()
    connection.close()

def insert(Item,Quantity,Price):
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(Item,Quantity,Price))
    connection.commit()
    connection.close()

insert('Wine Glass',10,15.5)

def view():
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("SELECT * from store")
    rows=cur.fetchall()
    connection.close()
    return rows

def delete(Item):
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("DELETE FROM store WHERE Item=?",(Item,))
    connection.commit()
    connection.close()

def update(Quantity,Price,Item):
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("UPDATE store SET Quantity=?,Price=? WHERE Item=?",(Quantity,Price,Item))
    connection.commit()
    connection.close()

update(1,100,"Water Glass")
delete("Wine Glass")
print(view())
