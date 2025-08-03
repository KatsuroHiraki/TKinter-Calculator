import tkinter as tk
from tkinter import messagebox

class myGUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text = "Your Message", font = ('Arial', 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 5, font = ('Arial', 16))
        self.textbox.pack(padx = 10, pady = 10)

        #CheckBox 
        self.checkVariable = tk.IntVar() #variable for checkbox
        self.check = tk.Checkbutton(self.root, text = "Show MessageBox", font = ('Arial', 16), variable = self.checkVariable)
        self.check.pack(padx = 10, pady = 10)

        self.showMessageButton = tk.Button(self.root, text = 'Show Message', font = ('Arial', 16), command = self.showMessage)
        self.showMessageButton.pack(padx = 10, pady = 10)

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing) #special command for window manager quit command

        self.root.mainloop()

    def showMessage(self):
        if self.checkVariable.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get('1.0', tk.END))

    def onClosing(self): #pop up message if quit window
        if messagebox.askyesno(title = "Quit ?", message = 'Do you really want to quit ?'):
            self.root.destroy()
        else:
            pass

# Create and run the app
app = myGUI()