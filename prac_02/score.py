"""
get score
evaluate score against parameters
print parameter

"""
import random

random_number = 0

def main():
    # pick random score, print score and rating
    score = random.randint(1, 100)
    print(score)
    score = score_rating(score)
    print(score)


def score_rating(score):
    # assign score rating
    while score > 0:
        if score < 50:
            return ("bad")
        elif score < 90:
            return ("passable")
        elif score <= 100:
            return ("Excellent")
        else:
            return ("invalid Score")





main()
