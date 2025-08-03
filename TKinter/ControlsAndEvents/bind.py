import tkinter as tk

def on_enter(event):
    label.config(text="Mouse over me!") #config to change text

def on_leave(event):
    label.config(text="Hover here")

root = tk.Tk()
label = tk.Label(root, text="Hover here", bg="lightblue")
label.pack(padx=10, pady=10)

#Mouse enter/leave
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

root.mainloop()
