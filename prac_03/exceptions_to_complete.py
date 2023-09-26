"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # check integer if True
    except ValueError:  # Use ValueError to catch exception
        print("Please enter a valid integer.")
print("Valid result is:", result)  # no danger of result being undefined
