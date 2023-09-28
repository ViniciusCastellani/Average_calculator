import tkinter as tk
from tkinter import simpledialog

# Function for calculating the average
def calculate_average():
    number1 = simpledialog.askfloat("Enter Number", "Enter the first number:")
    number2 = simpledialog.askfloat("Enter Number", "Enter the second number:")

    if number1 is not None and number2 is not None:
        average = (number1 + number2) / 2
        result_label.config(text=f"The average of the numbers is: {average:.2f}")
    else:
        result_label.config(text="Error in requesting values!")

# Create the main window
window = tk.Tk()
window.title("Average Calculator")

# Create a label to request values
result_label = tk.Label(window, text="")
result_label.pack(pady=20)

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate Average", command=calculate_average)
calculate_button.pack()

window.mainloop()

