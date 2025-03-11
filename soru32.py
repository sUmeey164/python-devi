#Lütfen argümanı kayan nokta sayılarından oluşan bir liste alan isimli bir fonksiyon yazınız .
#  Fonksiyon, orijinal listenin her bir öğesini dize biçiminde, iki ondalık basamağa yuvarlanmış olarak içeren yeni bir liste döndürür. 
# Listedeki öğelerin sırası değişmeden kalmalıdır.
def formatted(lst):
    # Use a list comprehension with f-strings to format each number to 2 decimal places
    return [f"{x:.2f}" for x in lst]

# Example usage:
my_list = [1.234, 0.3333, 0.11111, 3.446]
new_list = formatted(my_list)
print(new_list)  # ['1.23', '0.33', '0.11', '3.45']