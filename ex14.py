import random

def main():
    gen = number_gen()
    
    while True:
        ask = input("Try to guees a 4 digit number!: ")
        bulls = numb_guess(ask,gen)
        if bulls == 4:
            print("You guessed it!!")
            break    
def number_gen():
        while True: 
            num = str(random.randint(1000,9999))
            if len(set(num)) == 4:
                return num
                 
                
def numb_guess(guess,secretnumb):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secretnumb[i]:
            bulls+= 1
            
        elif guess[i] in secretnumb:
            cows+= 1
    print("Cows:",cows,"Bulls:",bulls) 
    return bulls
             
main()