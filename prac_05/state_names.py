"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
for state_code, state_name in CODE_TO_NAME.items():  # loop that prints all the states and names neatly lined up with string formattin
    print(f"{state_code:3} is {state_name}")

def main():
    state_code = get_state_code()

    while state_code != "":
        try:
            state_name = CODE_TO_NAME[state_code]
            print(state_code, "is", CODE_TO_NAME[state_code])
        except KeyError:
            print("Invalid short state")
        state_code = get_state_code()

def get_state_code():
    state_code = input("Enter short state: ")
    state_code = state_code.upper()
    return

main()