# Try contains code that may cause an error . except handles that error .

# Try block contains code that may cause an erro 

try:
    a = 10
    b = 0
    
    # This will cause ZeroDivisionError
    result = a/b
    
    print(result)
    
# Handles division by zero user 

except ZeroDivisionError:
    print("Cannot divide by zero")