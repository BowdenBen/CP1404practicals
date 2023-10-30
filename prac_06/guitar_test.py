

from guitar import Guitar


def main():
    """test the guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    ibanez = Guitar("Ibanez RGA42FM", 2016, 750)
    print(gibson)
    print(ibanez)
    print(f"{gibson.name} is {gibson.get_age()} years old")
    print(f"{ibanez.name} is {ibanez.get_age()} years old")
    print(f"{gibson.name} is {gibson.is_vintage()} ")
    print(f"{ibanez.name} is {ibanez.is_vintage()} ")

if __name__ == "__main__":
    main()