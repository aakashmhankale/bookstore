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
    cur.execute("INSERT INTO store VALUES('?,?,?')",(Item,Quantity,Price))
    connection.commit()
    connection.close()

insert('water glass',10,5)
