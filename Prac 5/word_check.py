
word_list = input('type sentence here:').split(' ')
word_dict = {}

for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
length = 0
for key in word_dict:
    if len(key) > length:
        longest_length = len(key)
    length = len(key)


for key in word_list:
    print("{:{}} : '{}' ".format(key, length+1, word_dict[key]))
