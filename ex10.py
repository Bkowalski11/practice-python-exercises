## Ask the user for a number and determine whether the number is prime or not.


a = int(input("Type an number: "))


def prime_numb(a):
    if a /2 %2 == 0:
        return print("Your number isn't a prime number!")
    else:
        return print("Your number is a prime number!")

prime_numb(a)