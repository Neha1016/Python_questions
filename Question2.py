# Palindrone number 

num4 = int(input("Enter a number to check palindrone or not :"))
num4_copy = num4
rev = 0
while num4 > 0:
    digit = num4 % 10
    rev = rev * 10 + digit
    num4 = num4 // 10

if num4_copy == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    
# Armstrong number

num5 = int(input("Enter a number to check armstrong or not :"))
num5_copy = num5
sum = 0
while num5 > 0:
    digit = num5 % 10
    sum += digit ** 3
    num5 //= 10

if num5_copy == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
    
    
# Count digit 

num6 = int(input("Enter a number to count digits :"))
count = 0
while num6 > 0:
    num6 //= 10
    count += 1

print(f"The number of digits in the number is: {count}")


# Multiplication Table

num7 = int(input("Enter a number to print multiplication table :"))
for i in range(1, 11):
    print(f"{num7} x {i} = {num7 * i}")
    

# Simple caculator

num8 = int(input("Enter first number: "))
num9 = int(input("Enter second number: "))
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter operation (1/2/3/4): ")

if operation == '1':
    print(f"The result is: {num8 + num9}")
elif operation == '2':
    print(f"The result is: {num8 - num9}")
elif operation == '3':
    print(f"The result is: {num8 * num9}")
elif operation == '4':
    print(f"The result is: {num8 / num9}")
else:
    print("Invalid operation.")
    

# Find GCD (Greatest Common Divisor )

num10 = int(input("Enter a number :"))
num11 = int(input("Enter a number :"))

while num11 != 0:
    num10, num11 = num11 , num10 % num11
    print(num10)
    
# Find LCM(Least Common Multiple )

num12 = int(input("Enter first number :"))
num13 = int(input("Enter second number :"))

a = num12
b = num12

while b!= 0:
    a, b = b, a % b 
    
gcd = a

lcm = (num12 * num13) //gcd   
print(f"The LCM of {num12} and {num13} is {lcm}")

# Print patterns (* , pyramid)

c = int(input("Enter a number :")) 

for i in range(1 , c + 1):
    for j in range(i):
        print("*" , end= " ")
    print()
       




