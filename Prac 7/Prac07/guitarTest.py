from guitar_script import Guitar

print('My Guitars')
guitars = []
new_guitar = [input("name:"), float(input("year:")), float(input("cost:$"))]
while new_guitar[0] != '':
    print("{} ({}) : ${}".format(new_guitar[0],new_guitar[1],new_guitar[2]))
    guitars.append(new_guitar)
    new_guitar = [input("name:"), float(input("year:")), float(input("cost:"))]

print('these are my guitars')
for i in range(len(guitars)):
    if guitars[i].is_vintage():
        vintage = "(vintage)"
    else:
        vintage = ""
    print("Guitar {}: {:20} ({}), worth ${} {}".format(i, guitars[i].name, guitars[i].year, guitars[i].cost, vintage))
