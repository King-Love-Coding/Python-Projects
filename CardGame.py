from random import choice
from time import sleep
from tkinter import Tk, Button, Label

Card1 = ["King", "Queen", "Jack", "Ace"]
Card2 = ["King", "Queen", "Jack", "Ace"]
Card3 = ["King", "Queen", "Jack", "Ace"]

root = Tk()
root.title("Card Game")

def play_game():
    choice1 = choice(Card1)
    choice2 = choice(Card2)
    choice3 = choice(Card3)
    result_label.config(text=f"{choice1}, {choice2}, {choice3}")
    if(choice1==choice2 and choice2==choice3):
        outcome_label.config(text="1000rs win")
    elif(choice1==choice2 or choice2==choice3 or choice3==choice1):
        outcome_label.config(text="500rs win")
    else:
        outcome_label.config(text="Looser => Submit 100rs")


result_label = Label(root, text="")
result_label.pack(pady=10)

outcome_label = Label(root, text="")
outcome_label.pack(pady=10)

play_button = Button(root, text="Play", command=play_game)
play_button.pack(pady=10)

root.mainloop()
