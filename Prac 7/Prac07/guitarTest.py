from guitar import Guitar

print('My Guitars')
guitars = []
name = input("name:")
while name != "":
    new_guitar = Guitar(name, 0, 0.0)
    new_guitar.year = int(input("year:"))
    new_guitar.cost = float(input("cost:"))
    print(new_guitar)
    guitars.append(new_guitar)
    name = input("name:")


for i in range(len(guitars)):
    if guitars[i].is_vintage():
        vintage = "(vintage)"
    else:
        vintage = ""
    print("{} {}".format(guitars[i],vintage))

