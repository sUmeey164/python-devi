#Please write a function named shortest, which takes a list of strings as its argument. 
# The function returns whichever of the strings is the shortest. If more than one are equally short, the function can return any of the shortest strings (there will be no such situation in the tests). You may assume there will be no empty strings in the list.

def shortest(strings):
   
    return min(strings, key=len)


my_list = ["first", "second", "fourth", "eleventh"]
result = shortest(my_list)
print(result)