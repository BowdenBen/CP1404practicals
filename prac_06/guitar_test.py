

from guitar import Guitar


def main():
    """test the guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    ibanez = Guitar("Ibanez RGA42FM", 2016, 750)
    print(gibson)
    print(ibanez)
    print(f"{gibson.name} is {gibson.get_age()} years old, expected 101 years old")
    print(f"{ibanez.name} is {ibanez.get_age()} years old, expected 7 years old")
    print(f"{gibson.name} is {gibson.is_vintage()}, expected True ")
    print(f"{ibanez.name} is {ibanez.is_vintage()}, expected False ")

if __name__ == "__main__":
    main()