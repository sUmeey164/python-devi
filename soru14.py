#Kullanıcıdan ekleme ve çıkarma arasında seçim yapmasını isteyen bir program yazınız. 
# Seçime bağlı olarak program, listenin sonuna bir öğe ekler veya listeden bir öğe çıkarır . 
# Eklenen öğenin listedeki son öğeden her zaman bir büyük olması gerekir. Eklenecek ilk öğenin 1 olması gerekiyor.
def main():
    num_list = []
    
    while True:
        print(f"The list is now {num_list}")
        choice = input("a(d)d, (r)emove or e(x)it: ").lower()
        
        if choice == 'd':
            if not num_list:
                num_list.append(1)
            else:
                num_list.append(num_list[-1] + 1)
        elif choice == 'r':
            if num_list:
                num_list.pop()
        elif choice == 'x':
            print("Bye!")
            break
        else:
            print("Invalid choice! Please enter 'd', 'r', or 'x'.")
    
    print(f"The final list is {num_list}")

if __name__ == "_main_":
    main()