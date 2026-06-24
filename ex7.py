import random

b = random.randint(1,9)

while True:
    a = input("Guess an number: ")
    if int(a) < b:
        print("Higher...")
        continue      
    if int(a) > b:
        print("Lower...")
        continue
    if int(a) == b:
        print("You guessed it!")
        break

    