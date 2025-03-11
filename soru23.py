#Lütfen anagramsiki stringi argüman olarak alan isimli bir fonksiyon yazınız. 
# Fonksiyon, Truedizelerin birbirinin anagramı olup olmadığını döndürür. 
# İki kelime eğer tam olarak aynı karakterleri içeriyorsa anagramdır.
def anagrams(str1, str2):
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage:
print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False