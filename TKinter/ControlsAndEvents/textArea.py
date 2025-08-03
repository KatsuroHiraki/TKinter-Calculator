import tkinter as tk

def print_text():
    print(text.get("1.0", tk.END))

root = tk.Tk()
text = tk.Text(root, height=5, width=30)
text.pack()

tk.Button(root, text="Submit", command=print_text).pack()

root.mainloop()
