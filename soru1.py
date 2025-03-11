#Please write a program which asks the user which editor they are using. 
# The program should keep on asking until the user types in Visual Studio Code.

while True:
    editor = input("Editör: ").strip().lower()
    
    if editor == "visual studio code":
        print("mükemmel bir seçim!")
        break
    elif editor in ["word", "notepad"]:
        print("berbat")
    else:
        print("iyi değil")
        