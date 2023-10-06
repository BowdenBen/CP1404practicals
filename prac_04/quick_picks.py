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
    number_of_quickpicks = int(input("How many quick picks do you want to generate? ")) # get userinput
    print("Quick Picks:") # print heading
    for i in range(number_of_quickpicks): # for instance in range of how many quickpicks to be generated
        quick_pick = generate_quick_pick() # generate a quickpick per instance
        print(" ".join(f"{number:2}" for number in quick_pick)) # right align each number in number list, join with a space inbetween, 1 number list per line

def generate_quick_pick():
    numbers = [] # create list
    while len(numbers) < NUMBERS_PER_QUICKPICK: # as long as there is less then 6 numbers, continue generating numbers
        number = random.randint(MIN_NUMBER, MAX_NUMBER) # generate numbers between 1 and 45 inclusive
        if number not in numbers: # check the number hasn't already been generated to avoid double ups
            numbers.append(number) # add number to list
    numbers.sort() # now list is full, sort from low to high
    return numbers # return the list to the main function

main()
