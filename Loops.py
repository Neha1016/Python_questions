# For Loop 

for i in range(6):
    print(i)
    
    
# While LOOP

i = 1

while i <= 10 :
    print(i)
    i += 1
    

# Nested Loop

for i in range(1,10):
    for j in range(1,10):
        print(i,j)
        
        
# Patter Printing 

rows = 5

for i in range( 1, rows +  1):
    print("* " * i)
    
    
# Inverted Star Pattern 

rows = 5

for i in range(rows, 0, -1):
    print("* " * i)
    
    
# Number Pattern

rows = 6

for i in range(1, rows + 1):
    for j in range(1, i + 1):
            print(j, end=" ")
    print()
    
    
# Same Number Pattern 

rows = 5 

for i in range(1, rows + 1):
    for j in range(1, i + 1):
            print(i, end=" ")
    print()
    
    
#  Print Numbers 1 to 10 

for i in range(1, 11):
    print(i)
    
# Even Numbers from 1 to 50

for i in range(2, 51, 2):
    print(i)
    
# Odd Numbers form 1 to 70 

for i in range(1, 71, 2):
    print(i)
    
# Sum of  First N Numbers 

n = int(input("Enter a number: "))

sum = 0 

for i in range(1, n + 1):
    sum += i
    
print(f"The sum of first {n} numbers is: {sum}")


# Multiplication Table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
    
# Factorial of a Number

num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i
    
print(f"The factorial of {num} is: {fact}")


# Fibonacci Series

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c 
    
print()  


# Prime Number Check

num = int(input("Enter a number: "))

count = 0 

for i in range(1, num + 1):
    if num % i == 0:
        count += 1
        
if count == 2 :
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    