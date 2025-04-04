from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    website = website_input.get()

    try:
        with open("data.json") as file:
            data = json.load(file)

        
        website_data = [object[website] for object in data if website in object][0]
        email = website_data["email"]
        password = website_data["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}, Password: {password}")

    except:
        messagebox.showinfo(title="Error", message="No Data File Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():

    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please make sure you haven't left any fields empty")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except:
            with open("data.json", "w") as file:
                json.dump([new_data], file, indent=4)
        
        else:
            with open("data.json", "w") as file:
                data.append(new_data)
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
canvas.grid(column=0, row=0)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", font=("Arial"))
website.grid(column=0, row=1)

website_input = Entry(width=21)
website_input.grid(column=1, row=1, columnspan=1)
website_input.focus()

website_button = Button(width=14, text="Search", command=search_website)
website_button.grid(column=2, row=1)

username = Label(text="Email/Username:", font=("Arial"))
username.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "abc@gmail.com")

password = Label(text="Password:", font=("Arial"))
password.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1)

password_button = Button(width=14, text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
