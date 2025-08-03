#pip install tkcalendar

from tkinter import *
from tkcalendar import DateEntry

root = Tk()

date = DateEntry(root, width=12, background='darkblue',
                 foreground='white', borderwidth=2)
date.pack(padx=10, pady=10)

root.mainloop()
