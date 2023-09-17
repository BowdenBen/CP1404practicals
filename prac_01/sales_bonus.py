"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""
get sales
while sales >= 0
    if sales are < $1000
    sales bonus = sales * 0.1
    print "Your Bonus is ()"
    elsif sales are >= $1000
    sales bonus = sales * 0.15
    print "Your Bonus is ()"
    else print "Your fired"   
"""

sales_actual = "What are your Sales?"
print(sales_actual)
sales = float(input("Enter sales: $"))
if sales > 0 < 1000:
    sales_bonus = sales * 0.1
    print(f"Your sales bonus is ${sales_bonus:.2f}")
elif sales >= 1000:
    sales_bonus = sales * 0.15
    print(f"Your sales bonus is ${sales_bonus:.2f}")
else:
    print("Your FIRED!")
print("Thank you")
