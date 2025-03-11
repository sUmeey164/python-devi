#Please write a function named same_chars, which takes one string and two integers as arguments. The integers refer to indexes within the string. The function should return True if the two characters at the indexes specified are the same. 
# Otherwise, and especially if either of the indexes falls outside the scope of the string, the function returns False.
def same_chars(s, index1, index2):
    if index1 < 0 or index2 < 0 or index1 >= len(s) or index2 >= len(s):
        return False
    return s[index1] == s[index2]

# Test cases
print(same_chars("programmer", 6, 7))  # True
print(same_chars("programmer", 0, 4))  # False
print(same_chars("programmer", 0, 12)) # False