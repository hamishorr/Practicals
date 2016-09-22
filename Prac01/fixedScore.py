loop = 1

while loop == 1:

    score = float(input("Input Score:"))

    if score < 0 or score > 100:
        print("Invalid score. Must be between 1 and 100")


    elif score > 100:
        print("Invalid score. Must be between 1 and 100")


    elif score > 50 and score < 90:
        print("Pass")
        loop = 0

    elif score > 90 and score <= 100:
        print("Excellent")
        loop = 0

    else:
        print("Fail")
        loop = 0