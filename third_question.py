#ask the user for a number
num = int(input("Please enter a number:"))

#define a list of divisors
divisors = []

'''check whether it is a prime number by:
going through each and every number that is smaller than that number and checking whether it is a divisor.
If the number has only 2 divisors (1 and itself) then it is a prime number.'''
for i in range(num):
    i += 1
    if num%i==0:
        divisors.append(i)

#checks whether the number has two divisors or not and print an appropriate statement
if len(divisors)==2:
    print("The number you entered is a prime number.")
else:
    print("The number you entered is not a prime number.")
