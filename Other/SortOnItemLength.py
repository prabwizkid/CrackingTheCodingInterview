# Sort a list based on the length of items
# Input: ["bob", "paris", "help", "an", "sydney"]
# Output: ["an", "bob", "help", "paris", "sydney"]
# Python dictionary was unordered before Python 3.6
# so sorted will work for both python 2 & 3


def sortOnLength(list):
    inddict = {}
    listr = []
    for i in range(0, len(list)):
        inddict[len(list[i])] = i
    for k, v in sorted(inddict.items()):
        listr.append(list[v])

    return listr


print(sortOnLength(["bob", "paris", "help", "ze", "sydney"]))

