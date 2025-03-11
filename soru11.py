#Lütfen üç fonksiyon yazınız: first_word, second_wordve last_word. Her fonksiyon bir string argümanı alır.
#İsimlerinden de anlaşılacağı üzere, fonksiyonlar dize argümanı olarak aldıkları cümlenin ilk, ikinci veya son kelimesini döndürür.
#Her durumda argüman dizisinin en az iki ayrı kelime içerdiğini ve tüm kelimelerin yalnızca bir boşluk karakteriyle ayrıldığını varsayabilirsiniz.
#  Argüman dizelerinin başında ve sonunda boşluk olmayacak.
def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1]

# Test cases
sentence = "it was a dark and stormy python"
print(first_word(sentence))  # it
print(second_word(sentence)) # was
print(last_word(sentence))   # python

sentence = "it was"
print(second_word(sentence)) # was
print(last_word(sentence))   # was