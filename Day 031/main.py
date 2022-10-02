from tkinter import *
from tkinter import messagebox
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")
IMG_FLASH_FRONT = "images/card_front.png"
IMG_FLASH_BACK = "images/card_back.png"
KNOWN_IMG = "images/right.png"
UNKNOWN_IMG = "images/wrong.png"
WORD_DATA = "data/french_words.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"

# Getting Data and set globals
current_card = {}
try:
    df = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    df = pandas.read_csv(WORD_DATA)
    word_dict = df.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    df = pandas.read_csv(WORD_DATA)
    word_dict = df.to_dict(orient="records")
else:
    word_dict = df.to_dict(orient="records")


# Button functions
def new_card():
    """Chooses a random word from word_dict, starts a 3-second timer and changes the canvas' style and text to the
       French current word. Will check if there are no more words. Takes no argument and returns nothing."""
    global current_card, flip_timer
    if len(word_dict) > 0:
        root.after_cancel(flip_timer)
        current_card = random.choice(word_dict)
        canvas.itemconfig(title_txt, text="French", fill="black")
        canvas.itemconfig(word_txt, text=current_card["French"], fill="black")
        canvas.itemconfig(canvas_image, image=img_flash_front)
        flip_timer = root.after(3000, func=flip_card)
    else:
        messagebox.showinfo("No more Words", "There are no more words to learn for you.\n"
                                             "Restart the program to start over.")


def flip_card():
    """'flips' the card to the 'back' and displays the english translation of the current French word.
        Takes no Arguments and returns nothing."""
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=img_flash_back)


def remove_card():
    """Removes the current card from word_dict and saves the new list of words in a file that will used as data the
       next time the program will run. Then calls new_card(). Takes no Arguments and returns nothing."""
    if len(word_dict) > 0:
        word_dict.remove(current_card)
        pandas.DataFrame(word_dict).to_csv(WORDS_TO_LEARN, index=False)
        new_card()
    else:
        messagebox.showinfo("No more Words", "There are no more words to learn for you.\n"
                                             "Restart the program to start over.")


# GUI CREATION
root = Tk()
root.title("Flashy")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = root.after(3000, func=flip_card)

# Canvas
canvas = Canvas(root, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_flash_front = PhotoImage(file=IMG_FLASH_FRONT)
img_flash_back = PhotoImage(file=IMG_FLASH_BACK)
canvas_image = canvas.create_image(400, 263, image=img_flash_front)
title_txt = canvas.create_text(400, 150, text="Placeholder Title", font=FONT_TITLE)
word_txt = canvas.create_text(400, 263, text="Placeholder Word", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
img_unknown = PhotoImage(file=UNKNOWN_IMG)
button_unknown = Button(image=img_unknown, highlightthickness=0, command=new_card)
button_unknown.grid(row=1, column=0)

img_known = PhotoImage(file=KNOWN_IMG)
button_known = Button(image=img_known, highlightthickness=0, command=remove_card)
button_known.grid(row=1, column=1)

new_card()
root.mainloop()
