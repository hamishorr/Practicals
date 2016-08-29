
word_list = input('type sentence here:').split(' ')
word_dict = {}

for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

max_length = 0
for key in word_dict:
    if len(key) > max_length:
        max_length = len(key)

for key in word_list:
    print("{:{}} : '{}' ".format(key, max_length + 1, word_dict[key]))
