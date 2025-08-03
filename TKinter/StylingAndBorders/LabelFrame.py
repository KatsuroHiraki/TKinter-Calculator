import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("LabelFrame Example")
root.geometry("300x150")

frame = ttk.LabelFrame(root, text="User Info")
frame.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame, text="Name:", font = ('Arial', 10)).grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame).grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Age:", font = ('Arial', 10)).grid(row=1, column=0, padx=5, pady=5)
tk.Entry(frame).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
