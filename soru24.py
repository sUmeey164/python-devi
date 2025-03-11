#Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. 
# Palindromes are words which are spelled exactly the same backwards and forwards.

def palindromes(word):
    return word == word[::-1]

def main():
    while True:
        word = input("Please type in a palindrome: ")
        
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")


main()