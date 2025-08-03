import tkinter as tk

root = tk.Tk()
root.title("Border Styles")
root.geometry("400x120")

styles = ["flat", "raised", "sunken", "ridge", "groove", "solid"]

for i, style in enumerate(styles):
    frame = tk.Frame(root, borderwidth=4, relief=style)
    frame.pack(side=tk.LEFT, padx=5, pady=10)

    tk.Label(frame, text=style).pack(padx=10, pady=10)

root.mainloop()
