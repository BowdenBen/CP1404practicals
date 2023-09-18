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
    # setting variables
    score = 0
    rated_score = 0
    # display menu, request menu choice
    print("(G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit")
    choice = input(">>>  ").upper()
    # process choice
    while choice != "Q":
        if choice == "G":
            # score rating function
            score = int(input("What is your score? "))
            rated_score = valid_score(score)
        elif choice == "P":
            print(f"Your {score} is {rated_score} ")
        elif choice == "S":
            # print star function
            show_stars(score)
        else:
            print("Invalid choice")
        choice = input(">>>  ").upper()
    print("ThankYou")

def valid_score(rate):
    # assign score rating
    while rate > 0:
        if rate < 50:
            return ("bad")
        elif rate < 90:
            return ("passable")
        elif rate <= 100:
            return ("Excellent")
        else:
            return ("invalid Score")

def show_stars(score, pen = "*"):
    print(score * pen)



main()