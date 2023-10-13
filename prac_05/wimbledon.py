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
    display_results(champion_wins, countries)


def read_file(FILENAME):
    """ get file and read line by line, skipping first line"""
    champions_data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)       # skip first line
        for line in in_file:
            champions_data.append(line.strip().split(","))
    return champions_data

def count_champion_wins(champions_data):
    """ create dictionary of how many wins champions have """
    champion_wins = {}
    for champion in champions_data:     #
        champion_name = champion[2]     # 3rd value in champions_data
        if champion_name in champion_wins:
            champion_wins[champion_name] += 1
        else:
            champion_wins[champion_name] = 1
    return champion_wins


def get_countries(champions_data):
    countries = set()
    for champion in champions_data:
        countries.add(champion[1])
    return sorted(countries)

def display_results(champion_wins, countries):
    print("Champions and their number of wins:")
    for team, wins in champion_wins.items():
        print(f"{team}: {wins} times")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()




