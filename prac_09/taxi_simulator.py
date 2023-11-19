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
def drive_taxi(current_taxi, bill_to_date):
    """ Handle the fare calculation in relation to drive distance"""
    is_valid_input = False      # set in put to false for error checking
    while not is_valid_input:
        try:
            distance = int(input("Drive distance? "))
            if 0 > distance:
                distance = int(input("Invalid. Drive distance? "))
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid distance.")
    current_taxi.start_fare()
    current_taxi.drive(distance)
    current_fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip has a total cost of ${current_fare:.2f}")
    return current_fare + bill_to_date


def choose_taxi():
