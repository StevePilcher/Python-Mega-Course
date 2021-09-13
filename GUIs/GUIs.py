from tkinter import *

window = Tk()


def kg_convertor():
    grams = float(e1_value.get()) * 1000
    lbs = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, lbs)
    t3.insert(END, ounces)


b1 = Button(window, text='Convert', command=kg_convertor)
b1.grid(row=1, column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1, column=2)

t1 = Text(window, height=1, width=5)
t1.grid(row=2, column=1)

t2 = Text(window, height=1, width=5)
t2.grid(row=2, column=2)

t3 = Text(window, height=1, width=5)
t3.grid(row=2, column=3)

window.mainloop()
