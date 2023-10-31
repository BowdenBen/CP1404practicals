"""
Write program to build a list of guitars, and signify whether they are vintage or not
time estimate: 2 hours
actual time: 5 hours
"""
from guitar import Guitar

def main():
    """Get a list of guitars and print them out"""
    guitars = guitar_list()

    for i, guitar in enumerate(guitars, 1):
        vintage = guitar.is_vintage()
        print(f"Guitar {i}: {guitar.name:>15} ({guitar.year:>4}), costs ${guitar.cost:>6,.2f}  (Considered {vintage})")


def guitar_list():
    """Make guitar list, populate list of lists with inputs, error check"""
    guitars = []
    print("Please enter the Guitars name, year of manufacture and cost. (Press enter to finish)")
    while True:
        name = input("Name: ")
        if not name:
            break
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid input. Please enter valid year.")
        try:
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid input. Please enter valid cost.")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        print(guitars)
    return guitars


if __name__ == "__main__":
    main()
