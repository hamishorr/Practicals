def main():

    print("asci number range selector, press q to quit")
    lower = input("input lower asci value:")
    upper = input("input upper asci value")

    finished = False

    while not finished:
        if not lower.isdecimal() or not upper.isdecimal():
            print("enter integer values. floats and other characters are not accepted")

        elif int(lower) >= 48 and int(upper) <= 58:
            get_number(lower, upper)
            finished = True

        else:
            print("incorrect numerical asci values, choose a number between 48 and 58")
        lower = input("input lower asci value:")
        upper = input("input upper asci value:")

    print('thank-you for using asci finder')

def get_number(lower,upper):
    for i in range(int(lower), int(upper) + 1, 1):
        print("{:3} {:2}".format(i, chr(i)))
    return()

main()
