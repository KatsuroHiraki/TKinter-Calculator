import tkinter as tk

def check_state():
    print("Checked?" , var.get())

root = tk.Tk()
var = tk.BooleanVar()

chk = tk.Checkbutton(root, text="I agree", variable=var, command=check_state)
chk.pack()

root.mainloop()
