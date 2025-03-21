#Please write a function named distinct_numbers, which takes a list of integers as its argument. 
# The function returns a new list containing the numbers from the original list in order of magnitude, and so that each distinct number is present only once.
def distinct_numbers(numbers):
    
    return sorted(set(numbers))


my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list))  # [1, 2, 3]