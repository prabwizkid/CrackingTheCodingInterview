# Given a Phone Number and a list of words,
# Determine which of the words in the list of words are contained in the Phone Number
# 1 (800) 3569377 -> 1 (800) flowers
# 253 6368 -> clement or clemdot
# Input:
# phoneNumber = "3662277"
# words = ['foo', 'bar', 'baz', 'foobar', 'emo', 'cap', 'car', 'cat']


# O(W . N)
def phoneNumbers(phoneNumber, words):
    phoneDict = {'a': '2', 'b': '2', 'c': '2',
                 'd': '3', 'e': '3', 'f': '3',
                 'g': '4', 'h': '4', 'i': '4',
                 'j': '5', 'k': '5', 'l': '5',
                 'm': '6', 'n': '6', 'o': '6',
                 'p': '7', 'q': '7', 'r': '7', 's': '7',
                 't': '8', 'u': '8', 'v': '8',
                 'w': '9', 'x': '9', 'y': '9', 'z': '9'}

    contained = []

    for word in words:
        dialedNumber = ""
        for n in word:
            dialedNumber += phoneDict[n]
        if phoneNumber.find(dialedNumber) != -1:
            contained.append(word)

    return contained


print(phoneNumbers("3662277", ['foo', 'bar', 'baz', 'foobar', 'emo', 'cap', 'car', 'cat']))

