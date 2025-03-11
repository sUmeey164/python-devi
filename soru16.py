#Please write a program which asks the user to type in values and adds them to a list.
#  After each addition, the list is printed out in two different ways:

items = []

while True:
    new_item = int(input("New item: "))
    
    if new_item == 0:  
        print("Bye!")
        break
    
    items.append(new_item)  
    
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)}")