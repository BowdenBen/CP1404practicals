"""
Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
Ask the user for their email until they enter a blank one.
Use a separate function to extract a name from the email as in the example below.

Estimate: 60 minutes
Actual:    150 minutes
"""

email_to_name = {}

email = input("Please enter your email address: ")
while email != "":
    username, domain = email.split("@")
    if "." in username:
        first_name, last_name = username.split(".")
        correct_name = input(f"Is your name {first_name} {last_name}? (Y?N)").lower()
        if correct_name == "y":
            email_to_name[email] = " ".join(username.split("."))
        else:
            username = input("What is your name? ")
            email_to_name[email] = username
    else:
        first_name = username
        correct_name = input(f"Is your name {first_name} ? (Y?N)").lower()
        if correct_name == "y":
            email_to_name[email] = username
        else:
            username = input("What is your name? ")
            email_to_name[email] = username
    print(email_to_name)
    email = input("Please enter your email address: ")
print("Thankyou")