"""
Use a constant dictionary of about 10 colour names and write a program that allows a user to enter a name and get the
code, e.g., entering AliceBlue (or aliceblue - make it case-independent) should show #f0f8ff.

Entering an invalid colour name should not crash the program.
Allow the user to enter names until they enter a blank one to stop the loop.
"""
COLOUR_TO_CODE = {"absolute zero": "0048ba", "acid Green": "b0bf1a", "aliceBlue": "f0f8ff",
                  "alizarin crimson": "e32636", "amethyst": "9966cc",
                  "bright lavender": "bf94e4", "bright lilac": "d891ef", "bright maroon": "c32148",
                  "bright navy blue": "1974d2", "bright turquoise": "08e8de"}

colour = input("Please enter colour you want a code for: ")
colour = colour.lower()  # colour can now accept upper and lower case input
while colour != "":  # while something has been entered, allows to quit out of loop by hitting return
    try:
        print(colour, "is", COLOUR_TO_CODE[colour])  # if key entered is on the list, print  "key" is "key value"
    except KeyError:  # if key isn't on the list
        print("Invalid colour")
    colour = input("Please enter colour you want a code for: ")
    colour = colour.lower()
