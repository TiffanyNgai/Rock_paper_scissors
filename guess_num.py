# Guessing number
# Author: Tiffany Ngai
# Course delivered by KylieYing

import random


def user_guess(minimum, maximum):
    ans = random.randint(minimum, maximum)
    print(f"The computer has generated an integer is between {minimum} and {maximum}. Try to guess it!")
    user_input = int(input("Try guessing the integer: "))

    while user_input != ans:
        if user_input > ans:
            maximum = user_input
            print(f"The value you entered is too large, the integer is between {minimum} and {maximum}")
            user_input = int(input("Try again: "))
        else:
            minimum = user_input
            print(f"The value you entered is too small, the integer is between {minimum} and {maximum}")
            user_input = int(input("Try again: "))

    print(f"You've got the right answer, the number is indeed {ans}")


def computer_guess():
    print("TODOOOO")


user_guess(1, 10)

# min = 1
# max = 100
# ans = random.randint(min, max)
# print(f"The computer has generated an integer is between {min} and {max}. Try to guess it!")
# user_input = int(input("Try guessing the integer: "))
#
# while user_input != ans:
#     if user_input > ans:
#         max = user_input
#         print(f"The value you entered is too large, the integer is between {min} and {max}")
#         user_input = int(input("Try again: "))
#     else:
#         min = user_input
#         print(f"The value you entered is too small, the integer is between {min} and {max}")
#         user_input = int(input("Try again: "))
#
# print(f"You've got the right answer, the number is indeed {ans}")