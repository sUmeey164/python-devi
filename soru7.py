#Lütfen shapedört argüman alan isimli bir fonksiyon yazınız.
#  İlk iki parametre yukarıdaki gibi bir üçgeni ve onu çizmek için kullanılan karakteri belirtir.
#  İlk parametre aynı zamanda dikdörtgenin genişliğini belirtirken, üçüncü parametre ise yüksekliğini belirtir. 
# Dördüncü parametre dikdörtgenin dolgu karakterini belirtir. Fonksiyon önce üçgeni, sonra da altındaki dikdörtgeni yazdırır.
#Gerçek çıktı için fonksiyon lineyukarıdaki alıştırmadaki fonksiyonu çağırmalıdır.
#  Çözümünüzü bu alıştırmanın kodunun üstündeki alıştırmaya kopyalayın.
#  Lütfen fonksiyonda hiçbir şeyi değiştirmeyin
def line(length, character):
    print(character * length)

def shape(triangle_height, triangle_char, rect_width, rect_height, rect_char):
    # Print the triangle
    for i in range(1, triangle_height + 1):
        line(i, triangle_char)
    
    # Print the rectangle
    for _ in range(rect_height):
        line(rect_width, rect_char)
    
    print()  # Separate different shapes with a blank line

# Test cases
shape(5, "X", 5, 3, "*")
shape(2, "o", 2, 4, "+")
shape(3, ".", 0, 0, "")  # Only a triangle