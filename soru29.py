#Please write a function named length_of_longest, which takes a list of strings as its argument. 
#The function returns the length of the longest string.

def length_of_longest(strings):
    # Use the max function to find the string with the maximum length
    return len(max(strings, key=len))

# Example usage
my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result)