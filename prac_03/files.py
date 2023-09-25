


out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name,file=out_file)
out_file.close()



filename = "name.txt"
in_file = open(filename, "r")
text = in_file.read()
in_file.close()
print(f"Your name is {text}")


in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
result = number1 + number2
print(result)


