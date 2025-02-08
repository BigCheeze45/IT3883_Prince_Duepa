# Program Name: mpg_converter.py
# Course: IT3883/Section W02
# Student Name: Prince Duepa
# Assignment Number: Lab/Assignment 3
# Due Date: 02/23/2025
# Purpose: GUI based application to convert MPG to KM/L
# List Specific resources used to complete the assignment
#   * https://tkdocs.com/index.html

import tkinter as tk
from tkinter import ttk

# Constants
MPG_TO_KML = 0.425143707

def mpg_to_kml(mpg):
    """Convert MPG to KM/L"""
    return mpg * MPG_TO_KML

class MPGConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("MPG to KM/L Converter")
        self.geometry("300x150")

        # Create and configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # MPG Entry
        ttk.Label(self, text="Miles per Gallon:").grid(row=0, column=0, padx=5, pady=20, sticky="e")
        self.mpg_var = tk.StringVar()
        self.mpg_var.trace_add('write', self.update_conversion)  # Trace changes to the variable
        self.mpg_entry = ttk.Entry(self, textvariable=self.mpg_var)
        self.mpg_entry.grid(row=0, column=1, padx=5, sticky="w")

        # KM/L Display
        ttk.Label(self, text="Kilometers per Liter:").grid(row=1, column=0, padx=5, pady=20, sticky="e")
        self.kml_var = tk.StringVar(value="0.0")
        self.kml_label = ttk.Label(self, textvariable=self.kml_var)
        self.kml_label.grid(row=1, column=1, padx=5, sticky="w")

    def update_conversion(self, *args):
        try:
            # Get the value from the entry
            mpg_text = self.mpg_var.get()
            if mpg_text == "":
                self.kml_var.set("0.0")
                return
                
            # Convert to float and calculate
            mpg = float(mpg_text)
            kml = mpg_to_kml(mpg)
            
            # Update the result label with 2 decimal places
            self.kml_var.set(f"{kml:.2f}")
            
        except ValueError:
            # If the input is not a valid number, show 0.0
            self.kml_var.set("0.0")

if __name__ == "__main__":
    app = MPGConverter()
    app.mainloop()
