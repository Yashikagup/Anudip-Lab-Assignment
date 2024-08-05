#Q.1 Write a program for arithmatic operators
#Answer
num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number '))
add = num1 + num2
dif = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
power = num1 ** num2
modulus = num1 % num2
print('Sum of ',num1 ,'and' ,num2 ,'is :',add)
print('Difference of ',num1 ,'and' ,num2 ,'is :',dif)
print('Product of' ,num1 ,'and' ,num2 ,'is :',mul)
print('Division of ',num1 ,'and' ,num2 ,'is :',div)
print('Floor Division of ',num1 ,'and' ,num2 ,'is :',floor_div)
print('Exponent of ',num1 ,'and' ,num2 ,'is :',power)
print('Modulus of ',num1 ,'and' ,num2 ,'is :',modulus)
#Output :
#a = 7
#b = 8
#a & b = 0
#a | b = 15
#a ^ b = 15
#~a = -8
#a << 2 = 28
#b >> 2 = 2

#Q.2 Write a program for assignment operators
#Answer
  a = 10
 b = 5
 # Assignment operator
 c = a
 print("c = a:", c)  
 # Add AND assignment operator
 c += b
 print("c += b:", c)  
 # Subtract AND assignment operator
 c -= b
 print("c -= b:", c) 
 # Multiply AND assignment operator
 c *= b
print("c *= b:", c)  
 # Divide AND assignment operator
 c /= b
 print("c /= b:", c)  
 # Modulus AND assignment operator
 c %= b
 print("c %= b:", c)  
# Exponent AND assignment operator
 c **= b
 print("c *= b:", c)  
 # Floor division AND assignment operator
 c = 10  
 c //= b
int("c //= b:", c)  
 # Bitwise AND assignment operator
 c = 10  
 c &= b
 print("c &= b:", c)  
# Bitwise OR assignment operator
 c |= b
 print("c |= b:", c)  
 # Bitwise XOR assignment operator
 c ^= b
 print("c ^= b:", c)  
 #Bitwise left shift assignment operator
 c <<= b
 print("c <<= b:", c) 
 #Bitwise right shift assignment operator
 c = 10  
c >>= b
 print("c >>= b:", c)  

# Output:-

# c = a: 10
# c += b: 15  
# c -= b: 10  
# c *= b: 50  
# c /= b: 10.0
# c %= b: 0.0 
# c *= b: 0.0 
# c //= b: 2  
# c &= b: 0   
# c |= b: 5   
# c ^= b:0  
# c <<= b: 0
# c >>= b: 0


#Q.3Write a program for Bitwise operators 
#Answer
a = 7
b = 8

print("a =", a)
print("b =", b)

# Bitwise AND
print("a & b =", a & b)

# Bitwise OR
print("a | b =", a | b)

# Bitwise XOR
print("a ^ b =", a ^ b)

# Bitwise NOT
print("~a =", ~a)

# Left Shift
print("a << 2 =", a << 2)

# Right Shift
print("b >> 2 =", b >> 2)

#OUTPUT:
#a = 7
#b = 8
#a & b = 0
#a | b = 15
#a ^ b = 15
#~a = -8
#a << 2 = 28
#b >> 2 = 2


#Q.4 Write a program to calculate greatest of three numbers.
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