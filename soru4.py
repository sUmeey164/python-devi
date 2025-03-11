#Lütfen hash karakterlerinden oluşan bir kare çizen isimli bir fonksiyon yazınız .
#  Fonksiyon, karenin kenar uzunluğunu belirleyen bir argüman alır.
#Gerçek çıktı için fonksiyon lineyukarıdaki alıştırmadaki fonksiyonu çağırmalıdır.
#  Çözümünüzü bu alıştırmanın kodunun üstündeki alıştırmaya kopyalayın. Lütfen fonksiyonda hiçbir şeyi değiştirmeyin 

def line(length):
    print('#' * length)

def square_of_hashes(side_length):
    for _ in range(side_length):
        line(side_length)
    print()  # Print an empty line after the square

# Test cases
square_of_hashes(5)
square_of_hashes(3)