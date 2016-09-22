finished = False
result = 0
while not finished:

    result = input("input result:")

    try:
        1/int(result)


    except ValueError:
        result = input("Please enter a valid integer:")

    print("result is {}".format(result))
    finished = True