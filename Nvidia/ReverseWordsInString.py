# Reverse each word in a String of words
# Input: "Hi how are you doing"
# Output: "iH woh era uoy gniod"


def reverseWords(str):
    finalStr = ""
    word = []
    for c in str:
        if c == " ":
            print(word[::-1])
            finalStr += "".join(word[::-1]) + " "
            del word[:]
        else:
            word.append(c)
    finalStr += "".join(word[::-1])
    return finalStr

print(reverseWords("Hi how are you doing"))