#1.  Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
#Answer
num = int (input ("Enter any number to test whether it is odd or even:" ))

if (num % 2) == 0:

              print ("The number is even")

else:

              print ("The provided number is odd")

#Output:

#Enter any number to test whether it is odd or even:
#887

#2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
#Answer
 # input age
age = int(input("Enter Age : "))

# condition to check voting eligibility
if age >= 18:
    status = "Eligible"
else:
    status = "Not Eligible"

print("You are ", status, " for Vote.")
#OUTPUT:
 #RUN 1:
#Enter Age : 21
#You are  Eligible  for Vote.

#RUN 2:
#Enter Age : 17
#You are  Not Eligible  for Vote.

#3. Write a Python program that determines if a given year is a leap year or not.
#Answer
# Default function to implement conditions to check leap year  
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")  
# Taking an input year from user  
Year = int(input("Enter the number: "))  
# Printing result  
CheckLeap(Year)
#Output:
#Enter the number: 2004
#Given Year is a leap Year


#4. Create a Python program that checks if a user-given number is positive, negative, or zero.
#Answer
# Prompt the user to input a number, and convert the input to a floating-point number.
num = float(input("Input a number: "))

# Check if the number is greater than zero.
if num > 0:
   # If true, print that it is a positive number.
   print("It is a positive number")
# Check if the number is equal to zero.
elif num == 0:
   # If true, print that it is zero.
   print("It is zero")
else:
   # If the above conditions are not met, print that it is a negative number.
   print("It is a negative number")
#OUTPUT:
#Input a number: 150                                                
#It is positive number

#5.  Write a Python program that determines the largest of three numbers entered by the user.
#Answer
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a == b and b == c:
    print('a, b, and c are equal')
elif a == b and a > c:
    print('a and b are equal,but c is the largest number')
elif a == c and a > b:
    print('a and c are equal but b is the largest number')
elif b == c and b > a:
    print('b and c are equal but a is the largest number')
elif a == b and c > a:
    print('a and b are equal, but c is the largest number')
elif a == c and b > a:
    print('a and c are equal, but b is the largest number')
elif b == c and a > b:
    print('b and c are equal, but a is the largest number')
elif a > b and a > c:
    print('a is the largest number')
elif b > a and b > c:
    print('b is the largest number')
else:
    print('c is the largest number')
#OUTPUT:
#Enter the first number: 9
#Enter the second number: 8
#Enter the third number: 5
#a is the largest number