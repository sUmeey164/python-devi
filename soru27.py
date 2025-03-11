#Lütfen argüman olarak iki tam sayı listesi alan isimli bir fonksiyon yazınız . 
# Fonksiyon, iki orijinal listedeki her indeksteki öğelerin toplamlarını içeren yeni bir liste döndürür. 
# Her iki listenin de aynı sayıda öğeye sahip olduğunu varsayabilirsiniz.
def list_sum(list1, list2):
    # List comprehension ile iki listeyi karşılaştırarak toplama işlemi yapıyoruz
    return [x + y for x, y in zip(list1, list2)]

# Örnek kullanım:
a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))  # [8, 10, 12]