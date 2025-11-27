#Kushal_Midterm_1
# Import tkinter module
import tkinter as tk
from tkinter import StringVar

#Create the main window
main_window = tk.Tk()
main_window.geometry('450x300')
main_window.title('Serendipity Points')

#Global variables
expression = ""
input_text = StringVar()

#Creating functions
#Function to handle button click
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#Function to clear the input and output
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
    output_label.config(text="Result will appear here.")

#Function to compute the number of points got
def _get_points(books):
    if books < 0:
        raise ValueError
    if books == 0:
        return 0
    elif books <= 3:
        return 5 if books >= 2 else 0
    elif books <= 5:
        return 15
    elif books <= 7:
        return 30
    else:
        return 60


def btn_equal():
    global expression
    raw = input_text.get().strip() or expression
    try:
        books = int(raw)
        points = _get_points(books)
        message = f"You earned {points} points."
    except Exception:
        message = "Invalid input. Enter a non-negative whole number."
    output_label.config(text=message)
    expression = raw

#Creating widgets
instruction = tk.Label(
    main_window,
    text=(
        "Enter the number of books purchased this month. (As a whole number)")
    )

instruction.pack(pady=(10, 5))

#Input display
input_entry = tk.Entry(main_window, textvariable=input_text, width=25)
input_entry.pack(pady=10,padx=10)

#Buttons frame
btns_frame = tk.Frame(main_window, width=400, height=100, bg="grey")
btns_frame.pack(pady=6)

#Clear button
btn_clearing = tk.Button(
    btns_frame, text="Clear", fg="black", width=30, height=3, bd=0, bg="#eee",
    cursor="hand2", command=btn_clear
)
btn_clearing.grid(row=0, column=0, padx=1, pady=1)

#Compute button
btn_compute = tk.Button(
    btns_frame, text="Compute Points", fg="black", width=30, height=3, bd=0, bg="#eee",
    cursor="hand2", command=btn_equal
)
btn_compute.grid(row=0, column=1, padx=1, pady=1)

#Creating output label
output_label = tk.Label(main_window, text="Result will appear here.")
output_label.pack(pady=(8, 10))

input_entry.focus_set()
main_window.mainloop()