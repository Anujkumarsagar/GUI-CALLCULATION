# Certainly! Here's a description for the code you provided:

# This Python script uses the Tkinter library to create a basic graphical calculator application. The calculator features a user-friendly graphical interface with a minimalistic design. The main components of the application include a root window, result label, input text area, and a set of buttons for numerical input and arithmetic operations.

# The root window is configured to have fixed dimensions, a title, and a pleasing background color. The `result_label` is used to display the current mathematical expression being entered and its result. The `text` label provides an input area where users can see the expression they are building.

# The calculator buttons are styled using a dictionary, and each button is created and placed in a grid layout within the root window. The buttons include digits 0-9, arithmetic operators (+, -, *, /), a decimal point, an equals sign (=) to calculate results, and a "C" button for clearing the input and result.

# The script defines functions to handle button clicks. When a button is clicked, the appropriate action is taken:
# - If the "=" button is clicked, the `evaluate()` function is called to compute and display the result.
# - If the "C" button is clicked, the `Clear()` function is called to clear the input and result.
# - For other buttons, the expression displayed in the `result_label` is updated accordingly.

# Overall, this code creates a user-friendly graphical calculator that allows users to input and evaluate arithmetic expressions with ease. It's a great example of a simple GUI application using the Tkinter library in Python.

import tkinter as tk 
root = tk.Tk()
root.minsize(268,400)
root.maxsize(268,400)


root.title('Anuj \'s Callualtor')
root.config(bg="#f39cc8")

result_label = tk.Label(root, text="", font=("Arial", 20),bg="#faeef4",width=15,height=0)
result_label.grid(row=0, column=0, columnspan=4,padx=5,pady=5)
text = tk.Label(root, text="", font=("Arial", 20),bg="#faeef4",width=15,height=0)
text.grid(row=1, column=0, columnspan=4, padx=10, pady=0)

button_style = {"width": 5, "height": 2, "bg": "#faeef4", "font": ("Arial", 14)}

def evalutate():
    try:
        expression = result_label.cget("text")
        result = str(eval(expression))
        result_label.config(text = result)
        text.config(text = expression)
    except Exception as e :
        result_label.config(text= "Error in evaluate ")
        text.config(text = "")

def Clear():
    result_label.config(text = "")
    text.config(text= "")




def button_click(event):
    button_experrsion = event.widget.cget("text")
    if button_experrsion == "=":
        evalutate()

    elif button_experrsion == "C":
        Clear()

    else :
        current_text = result_label.cget("text")
        entered_text = current_text+button_experrsion
        result_label.config(text = entered_text)



    
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'  # Clear button
]

col = 0
ro = 2

for text_button in buttons:
    button  = tk.Button(root, text=text_button,**button_style)
    button.config(font={"Arial",2},borderwidth = 2)
    button.grid(row=ro, column=col,padx=5, pady=5 )
    col += 1
    if col > 3:
        col = 0
        ro += 1
    button.bind("<Button-1>",button_click)



# button1=tk.Button(root,text="Click me",command=hello)
# button1.pack()
root.mainloop()
