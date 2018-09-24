#asks the user for a number
num = int(input("Please enter a number:"))

#checks whether the number is odd or even and prints an appropriate message
if num%2==0:
    print("The number you entered is an even number.")

    #for the number to be a multiplier of four, it should be an even number.
    #So, if the number is odd, there is no need to check if the number is a multiplier of 4.
    #In this case, we only need to check whether the number is a multiplier of 4 or not only if the number is even.
    if num%4==0:
        print("The number you entered is also a multiplier of 4.")

else:
    print("The number you entered is an odd number.")
