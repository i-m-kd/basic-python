#this program is to check whether a number is positive or negative or zero
# User enters the number
number = int(input("Enter number: "))

# checking the number
if number < 0: print("The entered number is negative.") elif number > 0:
    print("The entered number is positive.")
elif number == 0:
    print("Number is zero.")
else:
    print("The input is not a number")
