def isUnique(str):
    
    if len(str) > 128:  # Assuming the string is an ASCII string
        return False
    
    char_set = [0]  # Initialize to start dynamic length increase
    
    for i in str:
        val = str.index(i)
        
        if char_set[val]:
            return False
        char_set.insert(val, True)
    
    return True


print(isUnique('abcdefghijkAa'))