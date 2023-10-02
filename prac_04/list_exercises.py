from statistics import mean

data = []

for i in range(5):
        while True:
                try:
                        number = float(input(f"Please enter a number {i + 1} "))
                        break
                except ValueError:
                        print("That is an invalid number")
        data.append(number)
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