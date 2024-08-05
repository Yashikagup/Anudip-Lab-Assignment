#Write a program to show the example of following.


#1.Function without Parameters:
#Answer
def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
#Output:
#Hello World!
#Outside function

#2.Function with Parameter:
#Answer
def hello_to_you(name):
    print(f"Hello {name}")
    
hello_to_you("Timmy")
hello_to_you("Kristy")
hello_to_you("Jackie")
hello_to_you("Liv")

#Output:
#"Hello Timmy"
#"Hello Kristy"
#"Hello Jackie"
#"Hello Liv"

#3.Function with Default Parameter:
#Answer
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Output:

#I am from Sweden
#I am from India
#I am from Norway
#I am from Brazil

#4.Function with Return Keyword:
#Answer
def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList


print(appendItem('notebook'))
print(appendItem('pencil'))
print(appendItem('eraser'))
#Output:
#['notebook']
#['notebook', 'pencil']
#['notebook', 'pencil', 'eraser']

#5.Recursion:

 #a) WAP to print factorial value of a given number using recursion.
 #Answer
def recur_factorial(n): 
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: "))  
# check is the number is negative  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))
#Output:
#Enter a number: 3
#The factorial of 3 is 6

 #b) WAP to display Fibonacci series up to 10 iteration using recursion.
 #Answer               
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = 10  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))
#Output:
#Fibonacci sequence:
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               