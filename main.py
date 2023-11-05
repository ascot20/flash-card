import tkinter
import pandas
import random

# constants
BACKGROUND_COLOR = "#B1DDC6"
delay = None

# import csv file
df = pandas.read_csv('./data/french_words.csv')
translations = df.to_dict('records')


# ------------------------Next word mechanism------------------------#
def change():
    global delay
    random_word = random.choice(translations)
    card_canvas.itemconfig(card_image, image=front_card)
    card_canvas.itemconfig(title, text='French', fill='black')
    card_canvas.itemconfig(word, text=random_word['French'], fill='black')

    delay = window.after(3000, flip, random_word)


def flip(random_word):
    card_canvas.itemconfig(card_image, image=back_card)
    card_canvas.itemconfig(title, text='English', fill='white')
    card_canvas.itemconfig(word, text=random_word['English'], fill='white')

    window.after_cancel(delay)


# ------------------------UI------------------------#
window = tkinter.Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
window.resizable(False, False)
window.iconbitmap(default='./images/me.ico')

# canvas
card_canvas = tkinter.Canvas(width=600, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = tkinter.PhotoImage(file='./images/new_card_front.png')
back_card = tkinter.PhotoImage(file='./images/new_card_back.png')
card_image = card_canvas.create_image(300, 200, image=front_card)
title = card_canvas.create_text(300, 100, text='', font=("Ariel", 32, "italic"))
word = card_canvas.create_text(300, 200, text='', font=("Ariel", 48, "bold"))
card_canvas.grid(column=0, row=0, columnspan=2)

# buttons
correct_image = tkinter.PhotoImage(file='./images/new_right.png')
correct_button = tkinter.Button(image=correct_image, command=change)
correct_button.grid(column=1, row=1)

wrong_image = tkinter.PhotoImage(file='./images/new_wrong.png')
wrong_button = tkinter.Button(image=wrong_image, command=change)
wrong_button.grid(column=0, row=1)

change()

window.mainloop()
