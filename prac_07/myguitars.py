"""
Write a program to read all of these guitars and store them in a list of Guitar objects, using the class Guitar.
Display using a loop.
Now sort the list by year (oldest to newest) and display them in sorted order
"""

import csv
from guitar import Guitar


"""Read guitar data from the CSV file, use Guitar class to sort"""
guitars = []
with open('guitars.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        name, year, cost = row
        year = int(year)
        cost = float(cost)
        guitars.append(Guitar(name, year, cost))

print("**Guitars**\n")
for guitar in guitars:
    print(guitar)