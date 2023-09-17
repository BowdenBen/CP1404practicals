def main():

    password = get_password()
    print_asterix(password)


def print_asterix(password):
    print("*" * len(password))


def get_password():
    minimum_password_length = 8
    password = input("Please enter a password with a minimum 8 characters: ")
    while len(password) < minimum_password_length:
        print("Password not long enough")
        password = input("Please enter a password with a minimum 8 characters: ")
    return password


main()
