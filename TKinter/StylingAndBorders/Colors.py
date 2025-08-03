import tkinter as tk

root = tk.Tk()
root.title("Color Example")

#fg : foreground(textcolor), bg : background color
label = tk.Label(root, text="Hello World", fg="white", bg="black", font=("Arial", 16))
label.pack(pady=20, padx=20)

root.mainloop()
