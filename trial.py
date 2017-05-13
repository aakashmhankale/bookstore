def view():
    connection=sqlite3.connect("lite.db")
    cur=connection.cursor()
    cur.execute("SELECT * FROM store")
    connection.commit()
    connection.close()
    return rows

print(view())
