"""
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.
Each line of numbers should be displayed in sorted (ascending) order.
Your code should produce output that matches this sample output (except the numbers are random):
How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICKPICK = 6

def main():
    number_of_quickpicks = int(input("How many quick picks do you want to generate? "))
    print("Quick Picks:")
    for i in range(number_of_quickpicks):
        quick_pick = generate_quick_pick()
        print(" ".join("{:2}".format(number) for number in quick_pick))

def generate_quick_pick():
    numbers = [] # create list
    while len(numbers) < NUMBERS_PER_QUICKPICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()
