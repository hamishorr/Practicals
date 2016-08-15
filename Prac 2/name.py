name = input("enter name:")
name_file = open("name.txt", mode='w')
name_file.write(name)
name_file.close()

