# Create a program that asks the user for a number and then prints out a list of all 
# the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly 
# into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = input("Type an number: ")
a = []
for r in range(1,int(num) + 1):
    if int(num) % r == 0:
        a.append(r)
print(a)