import sqlite3


def connect():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, purchasePrice integer, "
                "salePrice integer) ")
    conn.commit()
    conn.close()


def insert(name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO items VALUES (NULL, ?, ?, ?)", (name, purchasePrice, salePrice))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name=""):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE name=?", (name,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("UPDATE items SET name=?, purchasePrice=?, salePrice=? WHERE id=?", (name, purchasePrice, salePrice, id))
    conn.commit()
    conn.close()


connect()
# insert("club", 5, 2.5)
# delete(7)

update(5, "staff", 2, 4)
print(view())
print(search(name="sword"))