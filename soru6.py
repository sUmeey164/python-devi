#Please write a function named triangle, which draws a triangle of hashes, and takes one argument. The triangle should be as tall and as wide as the value of the argument.
#The function should call the function line from the exercise above for the actual printing out. Copy your solution to that exercise above the code for this exercise. Please don't change anything in the line function.

def trianglekarma(n):
    for i in range(1, n + 1):
        print('b ' * i)

# line: Gerçek çıktı için yukarıdaki fonksiyonu çağıran kod
trianglekarma(5)
print()
trianglekarma(2)