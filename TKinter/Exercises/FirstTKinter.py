import tkinter as tk #import first

root = tk.Tk() #creates window

root.geometry("800x500") #width x height

root.title("My First GUI") #Setting the title

#Label
label = tk.Label(root, text = "Helloooooo", font = ('Arial', 18))
label.pack()

#Textbox (Multi-line text input)
textbox = tk.Text(root, height = 3, font = ('Arial', 15))
textbox.pack(padx = 10)

#Entry (Single line input)
myEntry = tk.Entry(root)
myEntry.pack(pady = 10)
value = myEntry.get() #Get the value from the entry

#Button
myButton = tk.Button(root, text = "Click me !", font = ('Arial', 18))
myButton.pack(padx = 10, pady = 10)

anotherButton = tk.Button(root, text = "This is manually placed", font = ("Arial", 18), width = 20)
anotherButton.place(x = 500, y = 150)

#Frame
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight = 1)
buttonFrame.columnconfigure(1, weight = 1)
buttonFrame.columnconfigure(2, weight = 1)
buttonFrame.pack(fill = 'x') #fill the window 

#Create the buttons into the Frame
bt1 = tk.Button(buttonFrame, text = "1", font = ('Arial', 18))
bt1.grid(row = 0, column = 0, sticky = "WE", padx=5, pady=5)

bt2 = tk.Button(buttonFrame, text = "2", font = ('Arial', 18))
bt2.grid(row = 0, column = 1, sticky = "WE", padx=5, pady=5)

bt3 = tk.Button(buttonFrame, text = "3", font = ('Arial', 18))
bt3.grid(row = 0, column = 2, sticky = "WE", padx=5, pady=5)

bt4 = tk.Button(buttonFrame, text = "4", font = ('Arial', 18))
bt4.grid(row = 1, column = 0, sticky = "WE", padx=5, pady=5)

bt5 = tk.Button(buttonFrame, text = "5", font = ('Arial', 18))
bt5.grid(row = 1, column = 1, sticky = "WE", padx=5, pady=5)

bt6 = tk.Button(buttonFrame, text = "6", font = ('Arial', 18))
bt6.grid(row = 1, column = 2, sticky = "WE", padx=5, pady=5)


root.mainloop() # runs the app and waits for user interactions. MUST BE BELOW ALL WIDGETS



