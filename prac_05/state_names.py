"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
for state_code, state_name in CODE_TO_NAME.items(): # loop that prints all the states and names neatly lined up with string formattin
    print(f"{state_code:3} is {state_name}")

state_code = input("Enter short state: ")
state_code = state_code.upper()     # state_code can now accept upper and lower case input
while state_code != "":     # while state code doesn't equal nothing, allows to quit out of loop by hitting return
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])       # as long as the key on the list is entered, print  "key" is "key value"
    except KeyError:        # if key isn't on the list
        print("Invalid short state")
    state_code = input("Enter short state: ")
    state_code = state_code.upper()
