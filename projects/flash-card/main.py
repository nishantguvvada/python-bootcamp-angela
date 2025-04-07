BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

import pandas as pd
import random

fr_en_list = {}

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    odf = pd.read_csv("./data/french_words.csv")
    fr_en_list = odf.to_dict(orient="records")
else:
    fr_en_list = df.to_dict(orient="records")

random_word = {}

def next_card():
    global random_word, flip_timer
    random_word = random.choice(fr_en_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(default_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")
    canvas.itemconfig(default_image, image=card_back_image)

def is_known():
    fr_en_list.remove(random_word)
    data = pd.DataFrame(fr_en_list)
    data.to_csv("./data/word_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
canvas.grid(column=0, row=0, columnspan=2)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
default_image = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=is_known)
correct_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()


window.mainloop()