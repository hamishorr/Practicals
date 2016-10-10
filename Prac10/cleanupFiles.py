"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics/Christmas')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
os.mkdir('temp')

# loop through each file in the (original) directory
for filename in os.listdir('.'):


    # ignore directories, just process files
    if not os.path.isdir(filename):
        if filename.replace(' ', '') != filename:
            new_name = filename.replace(' ', '_')
        else:
            i = 1
            # first character is neglected
            length = len(filename)
            new_name = False
            while i < length-4:
                if not new_name:
                    if filename[i].upper() == filename[i]:
                        new_name = filename[0:i] + '_' + filename[i:length]
                        length = len(new_name)
                        i += 1
                else:
                    if new_name[i].upper() == new_name[i]:
                        new_name = new_name[0:i] + '_' + new_name[i:length]
                        length = len(new_name)
                        i += 1
                i += 1
        if new_name:
            new_name = new_name.replace('.TXT', '.txt')
            print(new_name)

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name

        shutil.move(filename, 'temp/' + new_name)


# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)
