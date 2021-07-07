#Import the module "math" to gain access to the basic mathematical functions
import math

#Asking the user for a  value to assign to "x"
x = float(input("Enter a value for x: "))

#Asking the user for a value to assign to "y"
y = float(input("Enter a value for y: "))

#Printing the value of "x" raised to the power of "y"
print("\n" + ""x" raised to the power "y" = " + str(x ** y) + "\n")

#Printing the value of log base 2 of "x"
print("Log base 2 of "x" = " + str(math.log(x,2)) + "\n")