# 1 Print Hello World

print('Hello World')

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