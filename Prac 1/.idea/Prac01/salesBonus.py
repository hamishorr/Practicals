"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Sales Amount:"))

while sales > 0:

    if sales < 1000:
        print("10% bonus!")
    else:
        print("15% bonus!")

    sales = float(input("Sales Amount:"))

print("Negative sales. Terminated..")