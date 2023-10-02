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

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
QUICK_PICK_NUMBERS = 6


def main():
    quickpicks()


def quickpicks():
    try:
        number_of_quickpicks = int(input("How many quick picks do you want to generate? "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return number_of_quickpicks

def quickpick_numbers():
    numbers = sorted(random.randint(MIN_NUMBER, MAX_NUMBER + 1) for number in range(1, QUICK_PICK_NUMBERS + 1))
    return numbers