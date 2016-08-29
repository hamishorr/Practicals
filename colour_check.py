colour_dict = {'ALICEBLUE': 'f0f8ff', 'AQUAMARINE1': '7fffd4', 'AZURE1': 'f0ffff', 'BEIGE': 'f5f5dc' }


lookup = input("input colour").upper()
while lookup != 'Q':
    if lookup in colour_dict:
        print('hec code is:{}'.format(colour_dict[lookup]))
    else:
        print('incorrect colour name!')
    lookup = input("input colour").upper()