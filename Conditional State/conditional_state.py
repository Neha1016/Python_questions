# If 

age = int(input("Enter your age :"))

if age >= 18:
    print("You are eligible to vote.")
    

# If else

num = int(input("Enter a number :"))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")
    

# If elif else

marks = int(input("Enter your marks :"))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
    
    
# Nested if 

age = int(input("Enter your age :"))
license = input("Do you have a driving license? (yes/no): ")

if age >= 18:
    if license == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")
else:
    print("You are underage and not eligible to drive.")