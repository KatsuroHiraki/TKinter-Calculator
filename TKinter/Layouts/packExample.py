#HBOX AND VBOX STYLE

import tkinter as tk

root = tk.Tk()
root.title("HBox with pack")
root.geometry("300x100")

#HBOX
btn1 = tk.Button(root, text="Button 1")
btn2 = tk.Button(root, text="Button 2")
btn3 = tk.Button(root, text="Button 3")

# HBox-like layout (side=LEFT)
btn1.pack(side=tk.LEFT, padx=5)
btn2.pack(side=tk.LEFT, padx=5)
btn3.pack(side=tk.LEFT, padx=5)


#VBOX
btn4 = tk.Button(root, text="Top")
btn5 = tk.Button(root, text="Middle")
btn6 = tk.Button(root, text="Bottom")

# VBox-like layout (default side=TOP)
btn4.pack(pady=5)
btn5.pack(pady=5)
btn6.pack(pady=5)

root.mainloop()
