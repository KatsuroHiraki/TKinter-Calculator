import tkinter as tk

calculation = ""

def add_to_calculator(symbol):
    global calculation
    calculation += str(symbol)
    textField.delete(1.0, "end")
    textField.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    
    try:
        result = str(eval(calculation))
        textField.delete(1.0, "end")
        textField.insert(1.0, result)

    except:
        clear_field()
        textField.insert(1.0, "ERROR..")


def clear_field():
    global calculation
    calculation = ''
    textField.delete(1.0, "end")



root = tk.Tk()
root.geometry('250x300')

textField = tk.Text(root, height = 1,  width = 17, font = ('Arial', 17))
textField.grid(columnspan = 4, pady = 5, padx = 10, row = 0, column = 0) #columnspan stretches from column 0 to column 4

bt1 = tk.Button(root, text = "1", command = lambda: add_to_calculator(1), width = 3, font = ('Arial', 14))
bt1.grid(row = 1, column = 0, pady = 5)

bt2 = tk.Button(root, text = "2", command = lambda: add_to_calculator(2), width = 3, font = ('Arial', 14))
bt2.grid(row = 1, column = 1, pady = 5)

bt3 = tk.Button(root, text = "3", command = lambda: add_to_calculator(3), width = 3, font = ('Arial', 14))
bt3.grid(row = 1, column = 2, pady = 5)

bt4 = tk.Button(root, text = "4", command = lambda: add_to_calculator(4), width = 3, font = ('Arial', 14))
bt4.grid(row = 2, column = 0, pady = 5)

bt5 = tk.Button(root, text = "5", command = lambda: add_to_calculator(5), width = 3, font = ('Arial', 14))
bt5.grid(row = 2, column = 1, pady = 5)

bt6 = tk.Button(root, text = "6", command = lambda: add_to_calculator(6), width = 3, font = ('Arial', 14))
bt6.grid(row = 2, column = 2, pady = 5)

bt7 = tk.Button(root, text = "7", command = lambda: add_to_calculator(7), width = 3, font = ('Arial', 14))
bt7.grid(row = 3, column = 0, pady = 5)

bt8 = tk.Button(root, text = "8", command = lambda: add_to_calculator(8), width = 3, font = ('Arial', 14))
bt8.grid(row = 3, column = 1, pady = 5)

bt9 = tk.Button(root, text = "9", command = lambda: add_to_calculator(9), width = 3, font = ('Arial', 14))
bt9.grid(row = 3, column = 2, pady = 5)

bt0 = tk.Button(root, text = "0", command = lambda: add_to_calculator(0), width = 3, font = ('Arial', 14))
bt0.grid(row = 4, column = 1, pady = 5)

bt_plus = tk.Button(root, text = "+", command = lambda: add_to_calculator("+"), width = 3, font = ('Arial', 14))
bt_plus.grid(row = 4, column = 3, pady = 5)

bt_minus = tk.Button(root, text = "-", command = lambda: add_to_calculator("-"), width = 3, font = ('Arial', 14))
bt_minus.grid(row = 3, column = 3, pady = 5)

bt_mul = tk.Button(root, text = "x", command = lambda: add_to_calculator("*"), width = 3, font = ('Arial', 14))
bt_mul.grid(row = 2, column = 3, pady = 5)

bt_div = tk.Button(root, text = "/", command = lambda: add_to_calculator("/"), width = 3, font = ('Arial', 14))
bt_div.grid(row = 1, column = 3, pady = 5)

bt_leftparenthesis = tk.Button(root, text = "(", command = lambda: add_to_calculator("("), width = 3, font = ('Arial', 14))
bt_leftparenthesis.grid(row = 4, column = 0, pady = 5)

bt_rightparenthesis = tk.Button(root, text = ")", command = lambda: add_to_calculator(")"), width = 3, font = ('Arial', 14))
bt_rightparenthesis.grid(row = 4, column = 2, pady = 5)

bt_clear = tk.Button(root, text = "C", command = clear_field, width = 9, font = ('Arial', 14))
bt_clear.grid(row = 5, column = 0, pady = 5, columnspan = 2)

bt_equal = tk.Button(root, text = "=", command = evaluate_calculation, width = 9, font = ('Arial', 14))
bt_equal.grid(row = 5, column = 2, pady = 5, columnspan = 2)

tk.mainloop()