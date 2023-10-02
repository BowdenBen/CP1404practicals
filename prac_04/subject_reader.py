"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for parts in data:
        print(f"{parts[0]} is taught by {parts[1]} to {parts[2]} students")


def get_data():
    data =[]
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n character
        parts = line.split(',')  # Split the line into parts around the ","
        parts[2] = int(parts[2])  # Convert the third part (index 2) to an integer
        data.append(parts)  # Add the parts to the data list as a sublist

    return data  # Return the list of lists containing the data
    input_file.close()


main()