#Lütfen range_of_listargüman olarak bir tamsayı listesi alan isimli bir fonksiyon yazınız.
#  Fonksiyon listedeki en küçük değer ile en büyük değer arasındaki farkı döndürür.

def range_of_list(lst):
    if not lst:
        return 0  # Return 0 if the list is empty
    
    min_val = min(lst)
    max_val = max(lst)
    return max_val - min_val

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)