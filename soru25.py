#Lütfen sum_of_positivesargümanı tam sayılardan oluşan bir liste alan isimli bir fonksiyon yazınız. 
# Fonksiyon listedeki pozitif değerlerin toplamını döndürür.
def sum_of_positives(lst):
    # Sum only the positive numbers in the list
    return sum(x for x in lst if x > 0)

# Example usage:
my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)