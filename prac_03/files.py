
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

filename = "name.txt"
in_file = open(filename, "r")
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

total = 0
in_file = open("numbers.txt", "r")
for line in range(2):
    total += int(in_file.readline())
in_file.close()
print(total)

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)
