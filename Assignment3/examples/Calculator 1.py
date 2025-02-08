from tkinter import *

# The function called when a number button is pressed
def number_action(num):
    if "Div. By Zero" in display.get():
        display.set("0")
    if display.get() == "0":
        display.set(str(num))
    else:
        display.set(display.get() + str(num))
# The function called when an operator button is pressed
def operator_action(opp):
    global value_1
    global operator
    if "Div. By Zero" in display.get():
        display.set("0")
    if opp == "+":
        operator = "+"
        if value_1 is None:
            value_1 = float(display.get())
            display.set("0")
        else:
            value_1 = value_1 + float(display.get())
            display.set("0")
    if opp == "-":
        operator = "-"
        if value_1 is None:
            value_1 = float(display.get())
            display.set("0")
        else:
            value_1 = value_1 - float(display.get())
            display.set("0")
    if opp == "*":
        operator = "*"
        if value_1 is None:
            value_1 = float(display.get())
            display.set("0")
        else:
            value_1 = value_1 * float(display.get())
            display.set("0")
    if opp == "/":
        operator = "/"
        if value_1 is None:
            value_1 = float(display.get())
            display.set("0")
        else:
            try:
                value_1 = value_1 / float(display.get())
            except ZeroDivisionError:
                display.set("Div. By Zero")
                value_1 = None
                operator = None
            display.set("0")
    if opp == "=":
        if value_1 is not None:
            if operator is None:
                display.set(str(value_1))
            elif operator == "+":
                display.set(str(value_1 + float(display.get())))
            elif operator == "-":
                display.set(str(value_1 - float(display.get())))
            elif operator == "*":
                display.set(str(value_1 * float(display.get())))
            elif operator == "/":
                try:
                    display.set(str(value_1 / float(display.get())))
                except ZeroDivisionError:
                    display.set("Div. By Zero")
                    value_1 = None
                    operator = None
        value_1 = None
        operator = None
    if opp == "CE":
        display.set("0")
        value_1 = None
        operator = None


root = Tk()
value_1 = None
operator = None

one_button = Button(root, text="1", height=3, width=7, command=lambda i=1: number_action(i))
two_button = Button(root, text="2", height=3, width=7, command=lambda i=2: number_action(i))
three_button = Button(root, text="3", height=3, width=7, command=lambda i=3: number_action(i))
four_button = Button(root, text="4", height=3, width=7, command=lambda i=4: number_action(i))
five_button = Button(root, text="5", height=3, width=7, command=lambda i=5: number_action(i))
six_button = Button(root, text="6", height=3, width=7, command=lambda i=6: number_action(i))
seven_button = Button(root, text="7", height=3, width=7, command=lambda i=7: number_action(i))
eight_button = Button(root, text="8", height=3, width=7, command=lambda i=8: number_action(i))
nine_button = Button(root, text="9", height=3, width=7, command=lambda i=9: number_action(i))
zero_button = Button(root, text="0", height=3, width=7, command=lambda i=0: number_action(i))
add_button = Button(root, text="+", height=3, width=7, command=lambda i="+": operator_action(i))
subtract_button = Button(root, text="-", height=3, width=7, command=lambda i="-": operator_action(i))
multiply_button = Button(root, text="*", height=3, width=7, command=lambda i="*": operator_action(i))
divide_button = Button(root, text="/", height=3, width=7, command=lambda i="/": operator_action(i))
equals_button = Button(root, text="=", height=3, width=7, command=lambda i="=": operator_action(i))
clear_button = Button(root, text="CE", height=3, width=7, command=lambda i="CE": operator_action(i))

display = StringVar()
display_label = Label(root, font=("Helvetica", 16), textvariable=display)
display.set("0")

one_button.grid(row=5, column=0)
two_button.grid(row=5, column=1)
three_button.grid(row=5, column=2)
four_button.grid(row=4, column=0)
five_button.grid(row=4, column=1)
six_button.grid(row=4, column=2)
seven_button.grid(row=3, column=0)
eight_button.grid(row=3, column=1)
nine_button.grid(row=3, column=2)
zero_button.grid(row=6, column=1)
add_button.grid(row=5, column=3)
subtract_button.grid(row=4, column=3)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=2, column=3)
equals_button.grid(row=6, column=3)
clear_button.grid(row=1, column=3)
display_label.place(x=10, y=10)

root.grid_rowconfigure(0, minsize=50)

root.mainloop()