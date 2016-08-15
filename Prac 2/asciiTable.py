lower = input("lower asci value:")
upper = input("upper asci value:")

for i in range(int(lower), int(upper) + 1, 1):
 print("{:3} {:2}".format(i, chr(i)))


