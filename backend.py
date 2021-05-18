import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

items_Sales = Table(
    "items_Sales",
    Base.metadata,
    Column("itemid", Integer, ForeignKey("items.itemid"))
)

sale_header = Table(
    "sale_header",
    Base.metadata,
    Column("sellid", Integer, ForeignKey("Sales.sellid")),
    Column("headerid", Integer, ForeignKey("total_table.headerid"))
)

class Items(Base):
    __tablename__ = "item"
    itemid = Column(Integer, primary_key=True)
    name = Column(String)
    purchasePrice = Column(Integer)
    salePrice = Column(Integer)
    items = relationship("Sales", backref=backref("items"))


class Sales(Base):
    __tablename__ = "sell_table"
    sellid = Column(Integer, primary_key=True)
    itemid = Column(Integer, ForeignKey("item.itemid"))
    name = Column(String)
    purchasePrice = Column(Integer)
    salePrice = Column(Integer)
    SalesHeaders = relationship(
        "SalesHeader", secondary=sale_header, back_populates="sell_table"
    )


class SalesHeader(Base):
    __tablename__ = "total_table"
    headerid = Column(Integer, primary_key=True)
    total = Column(Integer)
    sellids = relationship(
        "sell_table", secondary=sale_header, back_populates="total_table"
    )


def connect():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS item (itemid INTEGER PRIMARY KEY, name text, purchasePrice integer, "
                "salePrice integer) ")
    conn.commit()
    conn.close()


def sell_table():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS sell (sellid INTEGER PRIMARY KEY, itemid integer, name text, purchasePrice integer,"
        "salePrice integer) ")
    conn.commit()
    conn.close()


def total_table():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS total (headerid INTEGER PRIMARY KEY, total integer) ")
    conn.commit()
    conn.close()


def insert(name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO item VALUES (NULL, ?, ?, ?)", (name, purchasePrice, salePrice))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM item")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name=""):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM item WHERE name=?", (name,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(itemid):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM item WHERE itemid=?", (id,))
    conn.commit()
    conn.close()


def update(itemid, name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("UPDATE item SET name=?, purchasePrice=?, salePrice=? WHERE itemid=?",
                (name, purchasePrice, salePrice, id))
    conn.commit()
    conn.close()


def insert_sell(itemid, name, purchasePrice, salePrice):
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO sell VALUES (NULL, ?, ?, ?, ?)", (itemid, name, purchasePrice, salePrice))
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
    cur.execute("SELECT total from total")
    row = cur.fetchone()
    value = row["total"]
    conn.close()
    return value


def total():
    conn = sqlite3.connect("pfitems.db")
    cur = conn.cursor()
    cur.execute("insert into total(total) select sum(salePrice) from sell")
    conn.commit()
    conn.close()


connect()
sell_table()
total_table()
