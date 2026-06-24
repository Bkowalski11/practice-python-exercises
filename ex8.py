a = "Rock"
b = "Paper"
c = "Scissors"

while True:
    d = input("Choose between Rock, paper or scissors!: ")
    e = input("Choose between Rock, paper or scissors!: ")
    if d == e:
        print("Tie!")
        
    if d == b and e == a:
        print("Player 1 wins!")
        
    if d == a and e == b:
        print("Player 2 wins!")
        
    if d == c and e == a:
        print("PLayer 2 wins!")
        
    if d == a and e == c:
        print("Player 1 wins!")
        
    if d == c and e == b:
        print("Player 1 wins!")
        
    if d == b and e == c:
        print("Player 2 wins!")
        
    f = input("Do you want to play again?: ")
    if f == "Yes":
        continue
    else:
        break
    break