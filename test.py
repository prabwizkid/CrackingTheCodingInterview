# def print_directory_contents(path):
# Print full path of files and folders inside this path.
# If the subfolder has folder inside it, keep going on...
# You are allowed to use any libraries including os except os.walk function.

import os

def print_directory_contents(path):

    # path = os.path.join(path)

    dirs = os.listdir(path)

    for file in dirs:
        print(os.path.join(path, file))
        if os.path.isdir(file):
            print_directory_contents(os.path.join(path, file))

    pass


print_directory_contents('/Users/prabhathk/Desktop/projects/CrackingTheCodingInterview')

