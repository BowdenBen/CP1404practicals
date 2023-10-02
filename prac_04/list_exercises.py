from statistics import mean

data = []

for i in range(5):
        while len(data) < 5:
                try:
                        number = float(input(f"Please enter a number {i + 1} "))
                except ValueError:
                        print("Invalid number")
                        number = float(input(f"Please enter a number {i + 1} "))
                data.append(number)
print(f"The first number is {data[0]}")
print(f"The last number is {data[4]}")
print(f"The smallest number is {min(data)}")
print(f"The largest number is {max(data)}")
print(f"The average of numbers is {mean(data)}")