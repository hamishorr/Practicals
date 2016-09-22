print("enter 5 numbers")

numbers = [input('number 1:'),input('number 2:'),input('number 3:'),input('number 4:'),input('number 5:')]

print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[len(numbers)-1]))
