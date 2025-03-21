#Please write a function named everything_reversed, which takes a list of strings as its argument. 
# The function returns a new list with all of the items on the original list reversed. 
# Also the order of items should be reversed on the new list.

def everything_reversed(strings):
    # Reverse the list and then reverse each string in the list
    return [s[::-1] for s in strings[::-1]]

# Example usage
my_list = ["Hi", "there", "example", "one more"]
new_list = everything_reversed(my_list)
print(new_list)