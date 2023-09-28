"""
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit

list menu, score, print result, show stars, quit
get menu input
get score
rate score
print score in stars

"""


def main():
    """ setting variables"""

    rated_score = 0
    # display menu, request menu choice
    print("(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit")
    choice = input(">>>  ").upper()
    # process choice
    while choice != "Q":
        if choice == "G":
            # score rating function
            score = get_valid_score()
            print(score)
        elif choice == "P":
            # rate score
            rated_score = valid_score(score)
            print(f"Your {score} is {rated_score} ")
        elif choice == "S":
            # print star function
            show_stars(score)
        else:
            print("Invalid choice")
        choice = input(">>>  ").upper()
    print("ThankYou")


def get_valid_score():
    """ check score is valid"""
    score = int(input("Score:"))
    while score < 0 or score >= 100:
        print("error")
        score = int(input("Score:"))
    return score

def valid_score(rate):
    """assign score rating"""
    while rate > 0:
        if rate < 50:
            return "bad"
        elif rate < 90:
            return "passable"
        elif rate <= 100:
            return "Excellent"
        else:
            return "invalid Score"


def show_stars(score, pen="*"):
    """ show score in stars"""
    print(score * pen)


main()
