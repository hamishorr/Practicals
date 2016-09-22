'''Number of items, enter price of item, add up total, if over $100 take 10% and show discount amount, print post cost'''

price = 0

items = input("Number of Items:")



while items.isdecimal() == False:
    items = input("Error! Please number of Items:")


for i in range (1,int(items)+1,1):
    print("item no. {:} weight in kg:".format(i))
    price = price + float(input(""))

    i = i + 1


if price > 100:
    discount = price*0.1
    print("10% discount achieved. you save ${:.2f}".format(discount))
    print("Total shipping charge is ${:.2f}".format(price-discount))

else:
    print("No discount achieved! Consider shipping another item. ")
    print("Total shipping charge is ${:.2f}".format(price))
