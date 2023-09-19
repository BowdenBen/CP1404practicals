"""
display menu for converting celsius to fahrenheit and visa versa
get input for measurement
convert to opposing measurement
display conversion
"""
def main():
    """display menu and retrieve menu selection"""
    MENU = """C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        """celsius_to_fahrenheit function"""
        if choice == "C":
            celsius_to_fahrenheit()
        elif choice == "F":
        """fahrenheit_to_celsius function"""
            fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} F")


main()