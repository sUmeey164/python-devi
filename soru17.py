#Lütfen argüman olarak bir liste alan ve listenin uzunluğunu döndüren isimli bir fonksiyon yazınız .
def length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# Example usage:
my_list = [1, 2, 3, 4, 5]
result = length(my_list)
print("The length is", result)

# Another example:
result = length([1, 1, 1, 1])
print("The length is", result)