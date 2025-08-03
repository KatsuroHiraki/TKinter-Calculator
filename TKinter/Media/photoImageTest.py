import tkinter as tk

root = tk.Tk()

img = tk.PhotoImage(file="C:/Users/alfya/Desktop/DE ROAD/PythonPractice/TKinter/Media/test2.png")  # only .png/.gif

label = tk.Label(root, image=img)
label.pack()

root.mainloop()
