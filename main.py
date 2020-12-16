"""
A Program to store Pathfinder items with purchase and sale prices
"""

from tkinter import *
#import backend

window = Tk()

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="purchasePrice")
l2.grid(row=0, column=2)

l3 = Label(window, text="salePrice")
l3.grid(row=1, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

purchasePrice_text = StringVar()
e2 = Entry(window, textvariable=purchasePrice_text)
e2.grid(row=0, column=3)

salePrice_text = StringVar()
e3 = Entry(window, textvariable=salePrice_text)
e3.grid(row=1, column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View all", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Sell Item", width=12)
b6.grid(row=7, column=3)

b7 = Button(window, text="Close", width=12)
b7.grid(row=8, column=3)

window.mainloop()
