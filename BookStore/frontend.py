from tkinter import *
from backend import Database

database = Database()

# FUNCTIONS
# View All Function - tied to button
def view_all_command():
    # Ensure list book is empty before fetching
    list1.delete(0, END)
    # All search returns a tuple, iterate through
    for book in database.view():
        list1.insert(END, book)


# Search Entry Function - tied to button
def search_entry():
    # Ensure list book is empty before fetching
    list1.delete(0, END)
    # loop through the search returned. .get() method changes the var to a simple string
    for book in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, book)


def insert_entry():
    # Ensure list book is empty before fetching
    list1.delete(0, END)
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    clear_entries()
    for book in database.view():
        list1.insert(END, book)


# Update selected book from the list, only works after selecting the listed book
def update_entry():
    database.update(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), selected_book[0])
    clear_entries()
    list1.delete(0, END)
    for book in database.view():
        list1.insert(END, book)


def delete_entry():
    # Ensure list book is empty before fetching
    list1.delete(0, END)
    database.delete(selected_book[0])
    clear_entries()
    # Update the list display
    for book in database.view():
        list1.insert(END, book)


# List bound selected function. Finds the book you clicked on from the list
def get_selected_book(event):
    global selected_book
    clear_entries()
    index = list1.curselection()[0]
    selected_book = list1.get(index)
    e1.insert(END, selected_book[1])
    e2.insert(END, selected_book[2])
    e3.insert(END, selected_book[3])
    e4.insert(END, selected_book[4])


# Function to clear input cells (Could be simplified maybe ?
def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


# Programme layout with Tkinter language wrapped between window and window.mainloop
window = Tk()

window.wm_title("BookStore")

# Labels for entries
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Entry boxes
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# List box with scrollbar
list1 = Listbox(window, height=10, width=75)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)
# List binding method
list1.bind('<<ListboxSelect>>', get_selected_book)

# Create Scrollbar
scroll1 = Scrollbar(window)
scroll1.grid(row=3, column=2, rowspan=6)

# Configure Scrollbar
list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)

# Buttons, commands do not call the function as it would work on programme start !
b1 = Button(window, text="View All", width=12, command=view_all_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_entry)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=insert_entry)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_entry)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_entry)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
