"""
get number of items
get price of each item
work out total price of all items
apply %10 discount if total price is over $100
display total price
"""
total_price = 0
number_of_items = int(input("How many items? "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("How many items? "))
for i in range(number_of_items):
    item_price = float(input(f"Price of item {i + 1} $"))
    total_price += item_price
    if total_price >= 100:
        discount = total_price * 0.1
    else:
        discount = 0
print(f"The total price of your shop is ${total_price - discount} ")
