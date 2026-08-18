# Function Basic

def greet():
    print("Hello, welcome to the Python ")
    
greet()  # Calling the function


# Function with Parameters

def add(a,b):
    print(f"The sum of {a} and {b} is: {a + b}")
    
add(5, 10)  # Calling the function with arguments


# Function with Return Value

def square(n):
    return n * n

result = square(4)  # Calling the function and storing the return value

print(f"The square of 4 is: {result}")


# Function with Default Parameter

def greeting(name="Guest"):
    print(f"Hello, {name}")
    
greeting()  # Calling the function without argument
greeting("Charlie")  # Calling the function with argument


# Function with Multiple Paramters 

def multiply(a, b):
    return a * b

result = multiply(5, 3)  # Calling the function and storing the return value


# Recursive Function

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"The factorial of 5 is: {factorial(5)}")


# Recursive Function (Sum of N Numbers )

def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n - 1)

print(sum_of_n(5))


# lambda function 

add = lambda a, b: a + b
print(add(5, 3))


# Lambda with filter() function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  


# Lambda with map() function

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)


# Lambda with sorted() function

students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]

result = sorted(students, key=lambda x: x[1])

print(result)  