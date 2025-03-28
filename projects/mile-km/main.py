# Advanced Arguments

# Arguments with default values
# def function(a=1, b=2):
#     pass

# Unspecified number of non keyworded arguments / positional arguments
# type(*args) => tuple
# def add(*args):
#     pass

# def add(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result

# Unspecified number of keyworded arguments
# type(**kwargs) => dict
# def calculate(**kwargs):

# class Car:

#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")

import tkinter as tk

window = tk.Tk()

window.title("Mile to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.place(x=30, y=40)
my_label.grid(column=5, row=0)

def button_clicked():
    print("clicked")
    received = input.get()
    my_label.config(text=received)

button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=20, pady=20)

input = tk.Entry(width=40)
input.grid(column=2, row=2)

window.mainloop()