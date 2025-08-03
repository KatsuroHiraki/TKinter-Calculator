import tkinter as tk

root = tk.Tk()
root.title("Font Example")

label1 = tk.Label(root, text="Bold Italic", font=("Arial", 14, "bold italic"))
label2 = tk.Label(root, text="Serif", font=("Times New Roman", 12))
label3 = tk.Label(root, text="Sans-serif", font=("Helvetica", 12))

label1.pack(pady=5)
label2.pack(pady=5)
label3.pack(pady=5)

root.mainloop()
