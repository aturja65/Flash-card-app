from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
dict_data = pd.DataFrame.to_dict(data, orient="records")


def random_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(dict_data)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(change_tittle, text="French", fill="black")
    canvas.itemconfig(change, text=word["French"], fill="black")
    timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(change_tittle, text="English", fill="white")
    canvas.itemconfig(change, text=word["English"], fill="white")


def known():
    dict_data.remove(word)
    new_data = pd.DataFrame(dict_data)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    random_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
change_tittle = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
change = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=known)
right_button.grid(row=1, column=1)
window.mainloop()
