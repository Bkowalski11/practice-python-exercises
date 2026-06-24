numb = input("Type an number:")
four = (int(numb)/4 %1)
comp = (int(numb)/2 %1 )
if (comp) == 0.0:
    print("Your number is even") 
else:
    print("Your number is odd")
if (four) == 0.0:
    print("Your number is an multipule of 4!")
