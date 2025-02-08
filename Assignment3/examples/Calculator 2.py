import json
from tkinter import *

class ButtonWrapper:
    def __init__(self, id="", type=""):
        self.ID = id
        self.TYPE = type
        self.BUTTON_OBJ = None


# The function called when any button is pressed
def button_action(id):
    global buttons
    if "Div. By Zero" in display.get():
        display.set("0")
    if buttons[id].TYPE == 'DIGIT':
        number_action(id)
    elif buttons[id].TYPE == 'OPERATOR':
        operator_action(id)

def number_action(num):
    if display.get() == "0":
        display.set(str(num))
    else:
        display.set(display.get() + str(num))

def operator_action(opp):
    global value_1
    global operator
    if opp == "+":
        operator = "+"
        if value_1 is None:
            value_1 = float(display.get())
        else:
            value_1 = value_1 + float(display.get())
        display.set("0")
    if opp == "-":
        operator = "-"
        if value_1 is None:
            value_1 = float(display.get())
        else:
            value_1 = value_1 - float(display.get())
        display.set("0")
    if opp == "*":
        operator = "*"
        if value_1 is None:
            value_1 = float(display.get())
        else:
            value_1 = value_1 * float(display.get())
        display.set("0")
    if opp == "/":
        operator = "/"
        if value_1 is None:
            value_1 = float(display.get())
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
buttons = {}

# Read in the buttons.json file and save it as an array of dictionaries
with open("buttons.json", 'r') as fin:
    button_data = json.load(fin)

# For each dictionary in the list create the button, and the object to hold the metadata
for jsonButton in button_data:
    b = ButtonWrapper(id=jsonButton['ID'], type=jsonButton['TYPE'])  # Create the button meta data container (object)
    b.BUTTON_OBJ = Button(root, text=jsonButton['TEXT'], height=3, width=7,  # Create the button widget
                          command=lambda i=jsonButton['ID']: button_action(i))
    b.BUTTON_OBJ.grid(row=int(jsonButton['ROW']), column=int(jsonButton['COL']))  # Add the widget to the screen
    buttons[b.ID] = b  # Save the button to our global array of buttons


display = StringVar()
display_label = Label(root, font=("Helvetica", 16), textvariable=display)
display.set("0")

display_label.place(x=10, y=10)

root.grid_rowconfigure(0, minsize=50)

root.mainloop()