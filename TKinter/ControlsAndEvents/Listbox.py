import tkinter as tk

def show_selected(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        print("You selected:", listbox.get(index))

root = tk.Tk()
listbox = tk.Listbox(root, height=5)
items = ["Apple", "Banana", "Orange", "Mango"]
for item in items:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", show_selected)
listbox.pack(pady=10)

root.mainloop()
