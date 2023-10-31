
from guitar import Guitar

def main():
    """Control all functions, use class function to process list"""
    guitar_list = []
    new_guitar = get_guitar()
    guitar_list.append(new_guitar)
def get_guitar():
    """Get user input of list of guitars(lists), include year, price"""
    name = input("Please enter the guitar's name:  ")
    while name != "":
        try:
            year = int(input("Please enter the year the guitar was made:   "))
            while year > 0:
                name.append(yeay)
            else:
                year = int(input("That is an incorrect year. Please enter the year the guitar was made:   "))
        except ValueError:
            year = int(input("That is not a number. Please enter the year the guitar was made:   "))
        try:
            cost = float(input("How much did the guitar cost:   $"))
            while cost > 0:
                name.append(cost)
            else:
                cost = float(input("Please enter the correct amount. How much did the guitar cost:   $"))
        except ValueError:
            cost = float(input("That is not a price. How much did the guitar cost:   $"))
    else:
        print("Thank you")



if __name__ == "__main__":
    main()
