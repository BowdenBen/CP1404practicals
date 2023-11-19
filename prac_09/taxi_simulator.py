"""
Taxi Simulator Practical
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Get an input choice from MENU"""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        elif choice == 'c':
            current_taxi = taxis[choose_taxi(taxis)]
        elif choice != 'q':
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
def drive_taxi():
    """ Handle the fare calculation in relation to drive distance"""
    is_valid_input = False      # set in put to false for error checking
    while not is_valid_input:
        try:
            distance = int(input("Drive distance? "))
        except ValueError:
            print("Invalid distance.")




def choose_taxi():
