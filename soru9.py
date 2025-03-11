#Lütfen greatest_numberüç argüman alan isimli bir fonksiyon yazınız.
#  Fonksiyon üç değerden en büyüğünü döndürür.

def greatest_number(a, b, c):
    return max(a, b, c)

# Test cases
print(greatest_number(3, 4, 1))   # 4
print(greatest_number(99, -4, 7)) # 99
print(greatest_number(0, 0, 0))   # 0