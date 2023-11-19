"""
Taxi Simulator Practical
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Get an input choice from MENU"""
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")


def drive_taxi():



def choose_taxi():
