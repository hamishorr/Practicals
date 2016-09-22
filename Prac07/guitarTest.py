from Prac07.guitar import Guitar

print('My Guitars')
guitars = []
name = input("name:")
while name != "":
    year = int(input("year:"))
    cost = float(input("cost:"))
    guitars.append(Guitar(name, year, cost))
    print(guitars[-1])
    name = input("name:")

for guitar in guitars:
    if guitar.is_vintage():
        vintage = "(vintage)"
    else:
        vintage = ""
    print("{} {}".format(guitar, vintage))


