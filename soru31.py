#Please write a function named all_the_longest, which takes a list of strings as its argument. 
# The function should return a new list containing the longest string in the original list. 
# If more than one are equally long, the function should return all of the longest strings.

def all_the_longest(strings):
    # Find the maximum length
    max_length = max(len(s) for s in strings)
    # Return all strings that have the maximum length
    return [s for s in strings if len(s) == max_length]

# Example usage
my_list = ["first", "second", "fourth", "eleventh"]
result = all_the_longest(my_list)
print(result)