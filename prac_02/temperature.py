"""
display menu for converting celsius to fahrenheit and visa versa
get input for measurement
convert to opposing measurement
display conversion
"""
MENU = """C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"""


def main():
    """display menu and retrieve menu selection"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            # celsius_to_fahrenheit function
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            # fahrenheit_to_celsius function
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} F")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """ convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """ convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
