
age = 0

people = float(input("Number of people:"))

for i in range(1,int(people)+1,1):
    age = age + float(input("age of person {:}:".format(i)))

mean = round(age/people,none)

print("average age is {:}" .format(mean))
