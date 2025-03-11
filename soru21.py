#Lütfen kullanıcıdan pozitif bir tam sayı N girmesini isteyen bir program yazın. 
# Program daha sonra -N ile N dahil olmak üzere tüm sayıları yazdırır, ancak 0 sayısını yazdıramaz .
#  Her sayı ayrı bir satıra yazılmalıdır.


# Asking for user input
N = int(input("Please type in a positive integer: "))

# Check if the input is a positive integer
if N > 0:
    # Printing numbers between -N and N, excluding 0
    for i in range(-N, N + 1):
        if i != 0:
            print(i)
else:
    print("Please enter a positive integer.")