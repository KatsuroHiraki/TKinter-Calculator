import tkinter as tk
from tkinter import ttk

def selected(event):
    print("Selected:", combo.get())

root = tk.Tk()
combo = ttk.Combobox(root, values=["Red", "Green", "Blue"])

combo.current(0)
combo.bind("<<ComboboxSelected>>", selected)
combo.pack()

root.mainloop()
