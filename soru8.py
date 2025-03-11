#Please write a function named spruce, which takes one argument. 
# The function prints out the text a spruce!, and the a spruce tree, the size of which is specified by the argument.

def spruce(n):
    print("bir ladin!")  # Başlık
    # Ladin ağacının üst kısmı (yıldızlar)
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    # Ladin ağacının gövdesi
    print(' ' * (n - 1) + '*')

# line: Gerçek çıktı için yukarıdaki fonksiyonu çağıran kod
spruce(3)