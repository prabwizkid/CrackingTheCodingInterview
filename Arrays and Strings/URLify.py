# Method to replace all spaces in a string with '%20'
# Input 'Mr John Smith    ', 13
# Output 'Mr%20John%20Smith%20'

# Using String(Immutable)
def uRLify(str, length):
    result = ''
    for i in range(0, length):
        if str[i] == " ":
            result += "%20"
        else:
            result += str[i]
    return result


print(uRLify('Mr John Smith    ', 13))

# Using arrays
def uRLifyArray(str, trueLength):
    numberOfSpaces = countOfChar(str, 0, trueLength, ' ')
    newIndex = trueLength - 1 + (numberOfSpaces * 2)
    myArray = [0] * (newIndex + 1)

    if newIndex + 1 < len(str):
        str[newIndex + 1] = "\0"

    for oldIndex in range(trueLength - 1, -1, -1):
        if str[oldIndex] == ' ':
            myArray[newIndex] = '0'
            myArray[newIndex - 1] = '2'
            myArray[newIndex - 2] = '%'
            newIndex -= 3
        else:
            myArray[newIndex] = str[oldIndex]
            newIndex -= 1

    return ''.join(myArray)


def countOfChar(str, start, end, target):
    count = 0
    for i in range(start, end):
        if str[i] == target:
            count += 1
    return count


print(uRLifyArray('Mr John Smith    ', 13))