"""
get score
evaluate score against parameters
print parameter

"""
import random

random_number = 0


def main():
    """ get score and random score and rate both"""
    score = int(input("Enter score: "))
    remark = score_rating(score)
    print(f"{score} is {remark}")
    # pick random score, print score and rating
    score = random.randint(1, 100)
    remark = score_rating(score)
    print(f"random {score} is {remark}")


def score_rating(rate):
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


main()
