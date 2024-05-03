BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random


# ---------------------Picking Random Words/Translation----------------------------------- #

try:
    data = pandas.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
to_learn_words = data.to_dict(orient="records")
current_card = {}
french_words = []


def is_known_word():
    global current_card, to_learn_words
    to_learn_words.remove(current_card)
    my_file = pandas.DataFrame(to_learn_words)
    my_file.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer, french_words
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_words)
    french_words.append(current_card)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{french_word}", fill="black")
    canvas.itemconfig(card_background, image=old_image)
    flip_timer = window.after(3000, func=flip_card)
    is_known_word()

# ---------------------Flipping Card----------------------------------- #


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image=new_image)


window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Image Creation
old_image = PhotoImage(file="./images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=old_image)

card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_img, command=next_card)
unknown_btn.grid(row=1, column=0)
unknown_btn.config(highlightthickness=0, bg=BACKGROUND_COLOR)

right_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=right_img, command=next_card)
known_btn.grid(row=1, column=1)
known_btn.config(highlightthickness=0, bg=BACKGROUND_COLOR)

next_card()

window.mainloop()
