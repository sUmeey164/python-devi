#Lütfen , karakter karesini yazdıran ve iki argüman alan isimli bir fonksiyon yazınız .
#  İlk parametre karenin kenar uzunluğunu belirtir. 
# İkinci parametre kareyi çizmek için kullanılan karakteri belirtir.
#Gerçek çıktı için fonksiyon lineyukarıdaki alıştırmadaki fonksiyonu çağırmalıdır.
#  Çözümünüzü bu alıştırmanın kodunun üstündeki alıştırmaya kopyalayın. Lütfen fonksiyonda hiçbir şeyi değiştirmeyin
def line(length, character):
    print(character * length)

def square(side_length, character):
    for _ in range(side_length):
        line(side_length, character)
    print()  # Kareler arasında boş satır bırakmak için

# Test cases
square(5, "*")
square(3, "o")