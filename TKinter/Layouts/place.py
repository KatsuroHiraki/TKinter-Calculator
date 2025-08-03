import tkinter as tk

root = tk.Tk()
root.title("place() Function")
root.geometry("300x200")

b1 = tk.Button(root, text = "Bottom", bg = "lightblue", width = 20)
b2 = tk.Button(root, text = "Top", bg = "pink", width = 20)

b1.place(x = 100, y = 100)
b2.place(x = 100, y = 65)

root.mainloop()
