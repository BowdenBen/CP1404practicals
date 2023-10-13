"""
Write a program to read this file, process the data and display processed information.

the champions and how many times they have won.
the countries of the champions in alphabetical order
store the data in appropriate data structures, use list of lists, a dictionary and a set.

For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
The solution uses 4 functions including main.


"""
FILENAME = "wimbledon.csv"

def main():
    """ Main function"""
    champions_data = read_file(FILENAME)
    champion_wins = count_champion_wins(champions_data)
    countries = get_countries(champions_data)
    print("Champions and their number of wins:")
    for team, wins in champion_wins.items():
        print(f"{team}: {wins} times")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_file(FILENAME):
    """ get file and read line by line, skipping first line"""
    champions_data = []     # create champions_data list
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)       # skip first line
        for line in in_file:        # iterate through every line after line 1 in file
            champions_data.append(line.strip().split(","))      # add each line to list while formatting
    return champions_data

def count_champion_wins(champions_data):
    """ create dictionary of how many wins champions have """
    champion_wins = {}      # create dictionary called champions_wins
    for champion in champions_data:     # iterate through the champions_data list
        champion_name = champion[2]     # 3rd object in champions_data, stored in champion_name
        if champion_name in champion_wins:      # iterate through champion_wins
            champion_wins[champion_name] += 1       # if champion_name key exists in dictionary, add 1 to value
        else:
            champion_wins[champion_name] = 1       # if champion_name key doesn't exist in dictionary, add to dictionary
    return champion_wins


def get_countries(champions_data):
    """ get and list the countries in alphabetical order """
    countries = set()       # create an empty set called countries to add data to
    for champion in champions_data:     # iterate through the champions_data list
        countries.add(champion[1])      # for 2nd place in list of champions_data list, add object to countries
    return sorted(countries)           # sort countries in alphabetical order



main()




