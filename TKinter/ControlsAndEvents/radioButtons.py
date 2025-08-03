import tkinter as tk

def on_select():
    print("You chose:", var.get())

root = tk.Tk()
var = tk.IntVar()

tk.Radiobutton(root, text="Option 1", variable=var, value=1, command=on_select).pack()
tk.Radiobutton(root, text="Option 2", variable=var, value=2, command=on_select).pack()

root.mainloop()
