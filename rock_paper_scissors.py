# Rock paper scissors
# Author: Tiffany Ngai
# Course delivered by KylieYing

# Possible further improvement:
#   User interface can be added
#   Error handling procedure can be included
import random

rps_type = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}


def player_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True
    else:
        return False


def rps():
    print("Welcome to the classic rock paper scissors game.")
    user_input = input("Enter 'r' for rock, 'p' for paper and 's' for scissors: ")
    computer_input = random.choice(['r', 'p', 's'])
    print(f"Your choice: {rps_type[user_input]}          The computer's choice: {rps_type[computer_input]}")
    if user_input == computer_input:
        return "It's a tie"
    if player_win(user_input, computer_input):
        return "Congratz, you won!"
    return "Yay, I won!"

#print(rps())
