# Leap year check 

from math import factorial


year = int(input("Enter a year to check Leap year or not :"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print(f"It is a leap year : { year }")
else:
    print(f"It is not a leap year : { year }")
    
# Factorial of a numbeer 

num = int(input(" Enter a number to find factorial :"))
fact = 1

for i in range(1, num + 1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")


# Fibonacci series 

num1 = int(input("Enter a number to find fibonacci series :"))

a = 0 
b = 1

for i in range(num1):
    print(a, end = " ")
    c = a + b 
    a = b
    b = c
    
# Prime Number check 

num2 = int(input("Enter a number to check prime or not :"))

if num2 > 1 and num2 % 2 != 0 :
    print(f" It is a prime number :{num2}")
else:
    print(f" It is not a prime number :{num2}")
    
# reverse a number 

num3 = int(input("Enter a number to reverse it :"))

reverse = 0 

while num3 > 0:
    digit = num3 % 10
    reverse = reverse * 10 + digit
    num3 = num3 // 10
    
print(f"The reverse of the number is: {reverse}")

# Sum of digits of a number 

num3 = int(input("Enter a number to find sum of digits:"))
sum = 0 

while num3 > 0:
    digit = num3 % 10
    sum = sum + digit
    num3 = num3 //  10
print(f"The sum of digits of the number is: {sum}")