#Please write a program which first asks the user for the number of items to be added. Then the program should ask for the given number of values, one by one, and add them to a list in the order they were typed in. 
# Finally, the list is printed out.

num_items = int(input("How many items: "))
items = []
for i in range(1, num_items + 1):
    value = int(input(f"Item {i}: "))
    items.append(value)  
print(items)