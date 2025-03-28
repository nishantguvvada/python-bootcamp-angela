from tkinter import *

window = Tk()

window.title("Mile to Kilometers Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    return output.config(text=f"{km}")

def button_clicked():
    miles_to_km()

input = Entry(width=5)
input.grid(column=2, row=1)

miles = Label(text="Miles", font=("Arial"))
miles.grid(column=3, row=1)

is_equal = Label(text="is equal to", font=("Arial"))
is_equal.grid(column=1, row=2)

output = Label(text="0", font=("Arial"))
output.grid(column=2,row=2)

km = Label(text="Km", font=("Arial"))
km.grid(column=3, row=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)
button.config(padx=10, pady=10)







window.mainloop()