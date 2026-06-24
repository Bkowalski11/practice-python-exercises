a = input("Type an word: ")
b = a.casefold() [::-1]
if b.casefold() [::-1] == a:
    print("Your word is a palindrome") 
else:
    print("Your word isn't a palindrome")