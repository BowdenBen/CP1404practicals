"""

"""
from statistics import mean

data = [] # create list

while len(data) < 5:  # continue asking until 5 valid floats are entered
    try:
        number = float(input(f"Please enter a number {len(data) + 1}: "))
        data.append(number)     # add number to list
    except ValueError:          # check that float is entered
        print("Invalid input. Please enter a valid number.")

print(f"The first number is {data[0]}")
print(f"The last number is {data[4]}")
print(f"The smallest number is {min(data)}")
print(f"The largest number is {max(data)}")
print(f"The average of numbers is {mean(data)}")



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_id = input("Please enter your user name")
if user_id in usernames:
        print("Access Granted")
else:
        print("Access Denied")