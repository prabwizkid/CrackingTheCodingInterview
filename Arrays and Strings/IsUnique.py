# Implement an algorithm to determine if a String has all unique characters.
# What if you cannot use additional data structures?


def isUnique(str):
    
    if len(str) > 128:  # Assuming the string is an ASCII string
        return False
    
    char_set = [0] * 128  # Initialize to start dynamic length increase
    
    for i in str:
        val = str.index(i)
        
        if char_set[val]:
            return False
        char_set[val] = True
    
    return True


print(isUnique('abcdefghijkB'))