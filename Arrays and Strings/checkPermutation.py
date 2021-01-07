# Given two strings, write a method to decide if one is a permutation of the other


def checkPermutation(str1, str2):
    
    if len(str1) != len(str2):  # Permutations must be of same length
        return False

    char_set = {chr(i): 0 for i in range(128)}  # Create a Hash table with ascii keys

    for i in str1:
        char_set[i] += 1
    
    for i in str2:
        char_set[i] -= 1
        if char_set[i] < 0:
            return False
        
    return True

print(checkPermutation("abcd123", "123abcd"))

