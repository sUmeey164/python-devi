#Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. 
# If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

from collections import Counter

def most_common_character(s):
   
    count = Counter(s)
   
    return min(count, key=lambda x: (-count[x], s.index(x)))


first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))