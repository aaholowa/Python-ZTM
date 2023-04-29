# import random

# print("Welcome to the random number guessing game!!!")
# min = int(input("Enter the lower bound: "))
# max = int(input("Enter the higher bound: "))


# def guessing_game(min, max):
#     rando = random.randint(min, max)
#     print(rando)
#     guess = int(input(f"Guess a number between {min} and {max}"))

#     while guess != rando:
#         guess = int(input("Sorry thats the wrong number, please guess again: "))

#     return print("congrats you guessed the right number")


# guessing_game(min, max)

from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue
