min_pass_length = 8

password = input("Please enter a password with a minimum 8 characters: ")
while len(password) < min_pass_length:
    print("Password not long enough")
    password = input("Please enter a password with a minimum 8 characters: ")
print("*" * len(password))