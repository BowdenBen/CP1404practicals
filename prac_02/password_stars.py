def main():
    """ execute functions """
    password = get_password()
    print_asterix(password)


def print_asterix(password):
    """ print asterix to the length of the password"""
    print("*" * len(password))


def get_password():
    """ get password """
    minimum_password_length = 8
    password = input("Please enter a password with a minimum 8 characters: ")
    #  check if password meets requirements
    while len(password) < minimum_password_length:
        print("Password not long enough")
        password = input("Please enter a password with a minimum 8 characters: ")
    return password


main()
