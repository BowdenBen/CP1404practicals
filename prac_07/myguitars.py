"""
Write a program to read all of these guitars and store them in a list of Guitar objects, using the class Guitar.
Display using a loop.
Now sort the list by year (oldest to newest) and display them in sorted order
"""

import csv
from guitar import Guitar


def main():
    """Read guitar data from the CSV file, use Guitar class to sort"""
    guitars = []
    read_guitar_csv(guitars)
    add_new_guitar = input("Add another guitar? (yes/no): ").lower()
    while add_new_guitar != "no":
        new_guitar = get_new_guitar()
        guitars.append(new_guitar)
        add_new_guitar = input("Add another guitar? (yes/no): ").lower()
    else:
        print("Thank you")

    guitars.sort()      # sort by year made
    print("**Guitars**\n")
    for guitar in guitars:
        print(guitar)
    update_guitars_file(guitars)


def update_guitars_file(guitars):
    """Write all guitars to guitars.csv"""
    with open('guitars.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Year', 'Cost'])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def read_guitar_csv(guitars):
    """Read guitar list from csv file"""
    with open('guitars.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            name, year, cost = row
            year = int(year)
            cost = float(cost)
            guitars.append(Guitar(name, year, cost))


def get_new_guitar():
    """Prompt user for new guitar details and return a Guitar object."""
    name = input("Enter guitar name: ")
    year = int(input("Enter year of manufacture: "))
    cost = float(input("Enter cost: "))
    return Guitar(name, year, cost)


if __name__ == "__main__":
    main()
