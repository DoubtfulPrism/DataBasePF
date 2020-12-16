import sqlite3


def connect():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, purchasePrice integer, "
                "salePrice integer) ")
    conn.commit()
    conn.close()


def sell_table():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sell (iq INTEGER PRIMARY KEY, id integer, name text, purchasePrice integer, "
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
    cur.execute("UPDATE items SET name=?, purchasePrice=?, salePrice=? WHERE id=?",
                (name, purchasePrice, salePrice, id))
    conn.commit()
    conn.close()


def insert_sell(id, name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO sell VALUES (NULL, ?, ?, ?, ?)", (id, name, purchasePrice, salePrice))
    conn.commit()
    conn.close()


def view_sell():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sell")
    rows = cur.fetchall()
    conn.close()
    return rows

def sell_total():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(mysum) FROM(SELECT SUM(salePrice) FROM sell)")
    conn.close()
    return mysum


connect()
sell_table()
