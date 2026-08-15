# 1 Print Hello World

print('Hello World')

# Variable Assignment

var = 10 
var1 = "Hello"
var2 = 2.22

print(var)
print(var1)
print(var2)

# Data Types 

data_type1 = 15
data_type2 = "Python"
data_type3 = 4.22
data_type4 = True
data_type5 = [1,2,3,4,5]
data_type6 = (10,20,30,40,50)
data_type7 = {11,22,33,44,55}
data_type8 = {"a":1, "b":2, "c":3}
data_type9 = None
data_type10 = complex(2,3)
data_type11 = bytes(5)
data_type12 = bytearray(5)

print(type(data_type1))
print(type(data_type2))
print(type(data_type3))
print(type(data_type4))
print(type(data_type5))
print(type(data_type6))
print(type(data_type7))
print(type(data_type8))
print(type(data_type9))
print(type(data_type10))
print(type(data_type11))
print(type(data_type12))

# Input and Output 

input_name = input("Enter your name :")
input_age = input("Enter your age :")

print(f"Hello {input_name}, you are {input_age} years old.")
print("Hello " + input_name + ", you are " + input_age + " years old.")
print("Hello {}, you are {} years old.".format(input_name, input_age))
print("Hello %s, you are %s years old." % (input_name, input_age))
print("Hello {0}, you are {1} years old.".format(input_name, input_age))
print("Hello {name}, you are {age} years old.".format(name=input_name, age=input_age))
print("Name = " , input_name)
print("Age = " , input_age)

# Operators 

op1 = 10 
op2 = 5

print("Addition = " , op1 + op2)
print("Subtraction = " , op1 - op2)
print("Multiplication = " , op1 * op2)
print("Division = " , op1 / op2)
print("Floor Division = " , op1 // op2)
print("Modulus = " , op1 % op2)
print("Exponentiation = " , op1 ** op2)
print("Greater than = " , op1 > op2)
print("Less than = " , op1 < op2)

# Type Casting 

type_cast1 = int(3.14)
type_cast2 = float(10)
type_cast3 = str(2.22)
type_cast4 = bool(1)
t_p = "101"
t_p1 = int(t_p)

print(type(t_p))
print(type(t_p1))
print(t_p1 + 50)
print(type_cast1)
print(type_cast2)
print(type_cast3)

# Comments 

# This is a single line comment

print("This is a single line comment")

# This is a multi-line comment

print("This is a multi-line comment")

# 2 Add Two Numbers 

a = 10 
b = 56 
c = a + b 
print(f"The sum of {a} and {b} is {c}")


# Take two numbers and print their sum 

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
sum = num1 + num2 
print(sum)


# 3 Swap Two Numbers

d = 1234
e = 5678
f = d
d = e
e = f
print(f"After swapping, the value of d is {d} and the value of e is {e}")

# Find the largest of two numbers 
l = int(input("Enter first number :"))
m = int(input("Enter second number :"))

if l > m :
    print(f"{l} is the largest number :")
    
else :
    print(f"{m} is the largest number :")    
    
print(f"The largest number between {l} and {m} is {max(l,m)}")  

# even or odd number 

nn = int(input("enter a number to check even or odd :"))

if nn % 2 == 0:
    print(f" It is even number : {nn}")  
else:
    print(f" It is odd number : {nn}")    

# 4 check even or odd 

g = 14
h = 7 

if g % 2 == 0 :
    print(f"{g} is an  even number ")
else:
    print(f"{g} is odd number")

if h % 2 == 0 :
    print(f" {h}is an even number ")
else:
    print(f"{h} is odd number ")
    
    
# Check whether a number is positive or negative 

aa = int(input("Enter a number to check positive or negative :"))

if aa >= 0 :
    print(f" It is a positive number : {aa}")
else :
    print(f" It is a negative number : {aa}")
    
# 5 Largest of three numbers 

i = 78
j = 88 
k = 90 

if i > j and i > k :
    print(f"{i} is the largest number")
if j > k and j > i :
    print(f"{j} is the largest number") 
if k> j and k > i :
    print(f"{k} is the largest number ")  
print(f"The largest number among {i}, {j} and {k} is {max(i,j,k)}")
  
# Swap two nuumbers .   
v = 8989898989
s = 34456678
t = v
v = s 
s = t 
print (f"After swapping , the value of v is {v} and the value of s is {s} ") 

# Find the square and cube of a number 

bb = int(input("enter a number to find square and cube :"))

square = bb ** 2 
cube = bb ** 3 

print(f"The square of {bb} is {square } and the cube of {bb} is {cube}:")

# convert celsius to fahrenheit

celsius = float(input("Enter temperature in Celsius :"))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit is : {fahrenheit}")

# convert kilometers to meters .

cc = float(input("Enter distance in kilometers :"))

meters = cc * 1000

print(f"Distance in meters is : {meters}:")