#Please write a function named line, which takes two arguments: an integer and a string. The function prints out a line of text, the length of which is specified by the first argument. The character used to draw the line should be the first character in the second argument. 
# If the second argument is an empty string, the line should consist of stars.

def line(length: int, char: str):
    if not char:
        char = "*"
    else:
        char = char[0]
    print(char * length)


line(7, "%")
line(10, "LOL")
line(3, "")