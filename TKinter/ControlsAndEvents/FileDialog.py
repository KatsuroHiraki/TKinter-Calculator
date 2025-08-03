import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)

root = tk.Tk()
tk.Button(root, text="Open File", command=open_file).pack()

root.mainloop()
