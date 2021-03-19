# Given a string, write a function to check if it is a permutation of a palindrome
# Input: Tact Coa
# Output: True -- Ex: "taco cat", "atco cta"


def palindromePermutation(str):
    str = str.lower().replace(" ", "")
    strdict = {}
    for c in str:
        if c in strdict.keys():
            strdict[c] += 1
        else:
            strdict[c] = 1

    count = 0
    for n in strdict.values():
        if (n % 2) != 0:
            count += 1

    if count >= 2:
        return False
    else:
        return True


print(palindromePermutation("Tact Coa"))
print(palindromePermutation("abbba"))
print(palindromePermutation("aabbcbcc"))
print(palindromePermutation("a"))

