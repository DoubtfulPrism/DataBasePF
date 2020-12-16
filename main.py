"""
A Program to store Pathfinder items with purchase and sale prices
"""

from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(name_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(name_text.get(), purchasePrice_text.get(), salePrice_text.get())
    list1.delete(0, END)
    list1.insert(END, (name_text.get(), purchasePrice_text.get(), salePrice_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], name_text.get(), purchasePrice_text.get(), salePrice_text.get())


def add_list():
    backend.insert_sell(selected_tuple[0], name_text.get(), purchasePrice_text.get(), salePrice_text.get())
    list1.delete(0, END)
    for row in backend.view_sell():
        list2.insert(END, row)


window = Tk()

window.wm_title("Pathfinder 1e Items Sales")

l1 = Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = Label(window, text="purchasePrice")
l2.grid(row=0, column=2)

l3 = Label(window, text="salePrice")
l3.grid(row=1, column=0)

l4 = Label(window, text="Total")
l4.grid(row=12, column=0)

name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

purchasePrice_text = StringVar()
e2 = Entry(window, textvariable=purchasePrice_text)
e2.grid(row=0, column=3)

salePrice_text = StringVar()
e3 = Entry(window, textvariable=salePrice_text)
e3.grid(row=1, column=1)

total_text = StringVar()
e4 = Entry(window, textvariable=total_text)
e4.grid(row=12, column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list2 = Listbox(window, height=6, width=35)
list2.grid(row=6, column=0, rowspan=6, columnspan=2)

sb2 = Scrollbar(window)
sb2.grid(row=6, column=2, rowspan=6)

list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list2.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Add to list", width=12, command=add_list)
b6.grid(row=7, column=3)

b7 = Button(window, text="Sell Item", width=12)
b7.grid(row=8, column=3)

b8 = Button(window, text="Close", width=12, command=window.destroy)
b8.grid(row=9, column=3)

window.mainloop()
