"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
menu = ("(H)ello\n(G)oodbye\n(Q)uit\n")
name = (input("Enter name: "))
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello", name)
    elif choice == "G":
        print(f"Goodbye", name)
    else:
        print("Invalid selection")
    print(menu)
    choice = input(">>> ").upper()




