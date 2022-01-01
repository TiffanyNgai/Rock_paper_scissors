# Simple UI for rock paper scissors game using tkinter
#images taken from: https://www.vecteezy.com/vector-art/691497-rock-paper-scissors-neon-icons

from tkinter import *
from rock_paper_scissors import *
import sys
import os

user_choice = ""


def rps_ui(user_input):
    computer_input = random.choice(['r', 'p', 's'])
    Label(root, text=f"Your choice: {rps_type[user_input]}          The computer's choice: {rps_type[computer_input]}", font=('Arial', 20), bg="#FDECCB").pack(side=TOP)
    if user_input == computer_input:
        Label(root, text="It's a tie!", font=('Arial', 30), bg="#FDECCB").pack(side=TOP)
        return
    if player_win(user_input, computer_input):
        Label(root, text="Congratz, you won!", font=('Arial', 30), bg="#FDECCB").pack(side=TOP)
        return
    Label(root, text="Yay, I won!", font=('Arial', 30), bg="#FDECCB").pack(side=TOP)
    return


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)



def end_game():
    paper_button["state"] = DISABLED
    rock_button["state"] = DISABLED
    scissors_button["state"] = DISABLED
    restart_button = Button(root, text="Click to restart", font=("Arial", 20), command=restart_program, height=2, width=13, highlightbackground="#BDE4A7")
    restart_button.pack(side=TOP)



def paper_func():
    rps_ui("p")
    print("Paper button is clicked")
    end_game()


def rock_func():
    rps_ui("r")
    print("Rock button is clicked")
    end_game()


def scissors_func():
    rps_ui("s")
    print("Scissors button is clicked")
    end_game()


root = Tk()
root.title("Rock paper scissors")
root.geometry("1000x600")
root.config(bg="#FDECCB")


Label(root, text="Rock Paper Scissors", font=('Arial', 50), bg="#FDECCB").pack(side=TOP)
paper_icon = PhotoImage(file=r"paper_icon.png")
paper_button = Button(root, image=paper_icon, command=paper_func)
rock_icon = PhotoImage(file=r"rock_icon.png")
rock_button = Button(root, image=rock_icon, command=rock_func)
scissors_icon = PhotoImage(file=r"scissors_icon.png")
scissors_button = Button(root, image=scissors_icon, command=scissors_func)
paper_button.pack(side=TOP)
rock_button.pack(side=TOP)
scissors_button.pack(side=TOP)
root.mainloop()