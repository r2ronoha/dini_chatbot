#------------------------------------------------
# guessing_numbers.py
# version 1.0 (5 March 2023)
# Author: Idaisa Noha-Smith
#------------------------------------------------
# this game is a guessing numbers with hints game (higher & lower).
# we will pick a number wich you will not know then you have to guess the
# number we will give hints such as higher and lower.
#------------------------------------------------

import random

print("hello i am a game. to play guess numbers between 1-100")
random_number = random.randint(1,100)

print("what is your number?")
user_number = int(input())

while user_number != random_number:
    if user_number < random_number:
        print("try a bit higher.")
    else:
        print("try a bit lower.")
    user_number = int(input())

print("well done you guessed right.")
