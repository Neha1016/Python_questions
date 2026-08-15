
# try block contains code that may produce error

try:
    
    # Open the file in read mode
    file = open("ss.txt", "r")
    
    # Read the file
    data =  file.read()
    
    # Display the data
    print(data)
    
    # Close the file
    file.close()
    
    
# If the file does not exist,
# FileNotFoundError will be handled here 
except FileNotFoundError:
    print("File not found")
    
    
# Write File With Exception Handlind

try:
    file = open("ss.txt" , "w")
    
    file.write("Hello Python")
    file.write("\nFile Handling is easy.")
    
    file.close()
    
    print("Data written successfully")
    
except Exception:
    print("Something went wrong")
    
    
    
try:
    file = open("ss.txt" , "w")
    
    file.write("Hello Python")
    
    file.close()
    
    file.write("\nFile Handling is easy.")
        
    
    print("Data written successfully")
    
except Exception:
    print("Something went wrong")
    
    

try:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    
    print(a/b)
    
except ValueError:
    print("Please enter numbers only")
    
except ZeroDivisionError:
    print("Cannot divide by zero")