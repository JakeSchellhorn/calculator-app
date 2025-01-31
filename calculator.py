import tkinter as tk
root = tk.Tk()

#window properties
root.title("Calculator")
root.configure(background="yellow")
root.geometry("312x324")
root.resizable(0, 0)

#calculator functions

def btn_click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def btn_clear():
    global expression
    expression = ""
    equation.set("")
    
def btn_equal():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""

expression = ""
equation = tk.StringVar()

#calculator frame
frame = tk.Frame(root, width = 302, height = 314, bg = "blue")
frame.pack(padx = 10, pady = 10)

input_frame = tk.Frame(frame, width = 302, height = 100, bg = "silver")
input_frame.pack(side="top")
input_field = tk.Entry(input_frame, textvariable = equation, justify = "right")
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10, ipadx = 70)

button_frame = tk.Frame(frame, width = 302, height = 264, bg = "silver")
button_frame.pack(padx = 10, pady = 10)


#row 1
clear = tk.Button(button_frame, text = "C", width = 30, height = 2, 
                  command = lambda: btn_clear()).grid(row=0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = tk.Button(button_frame, text = "/", width = 5, height = 2, 
                   command = lambda: btn_click("/")).grid(row = 0, column = 4, padx = 1, pady = 1)

#row 2
seven = tk.Button(button_frame, text = "7", width = 9, height = 2, 
                  command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 0, pady = 1)
eight = tk.Button(button_frame, text = "8", width = 9, height = 2, 
                  command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 0, pady = 1)
nine = tk.Button(button_frame, text = "9", width = 9, height = 2, 
                 command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 0, pady = 1)
multiply = tk.Button(button_frame, text = "x", width = 5, height = 2, 
                     command = lambda: btn_click("*")).grid(row = 1, column = 4, padx = 1, pady = 1)

#row 3
four = tk.Button(button_frame, text = "4", width = 9, height = 2, 
                  command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 0, pady = 1)
five = tk.Button(button_frame, text = "5", width = 9, height = 2, 
                  command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 0, pady = 1)
six = tk.Button(button_frame, text = "6", width = 9, height = 2, 
                 command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 0, pady = 1)
subtract = tk.Button(button_frame, text = "-", width = 5, height = 2, 
                     command = lambda: btn_click("-")).grid(row = 2, column = 4, padx = 0, pady = 1)

#row 4
one = tk.Button(button_frame, text = "1", width = 9, height = 2, 
                  command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 0, pady = 1)
two = tk.Button(button_frame, text = "2", width = 9, height = 2, 
                  command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 0, pady = 1)
three = tk.Button(button_frame, text = "3", width = 9, height = 2, 
                 command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 0, pady = 1)
add = tk.Button(button_frame, text = "+", width = 5, height = 2, 
                     command = lambda: btn_click("+")).grid(row = 3, column = 4, padx = 0, pady = 1)

#row 5
zero = tk.Button(button_frame, text = "0", width = 30, height = 2, 
                  command = lambda: btn_click(0)).grid(row=4, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = tk.Button(button_frame, text = "=", width = 5, height = 2, 
                   command = lambda: btn_equal()).grid(row = 4, column = 4, padx = 1, pady = 1)



root.mainloop()