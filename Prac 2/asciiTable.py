def main():
    get_number(int(input("input lower asci value:")), int(input("input upper asci value")))

def get_number(lower,upper):
    for i in range(int(lower), int(upper) + 1, 1):
        print("{:3} {:2}".format(i, chr(i)))

main()
