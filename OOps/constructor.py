# A constructor is automatically called when an object is created . 
# In python , __init__() is commonly used as the constructor .

# Define a student class 
class Student:
    
    # Constructor
    # It runs automatically when an object is created 
    def __init__(self, name, age):
        
        # Store values in object variables
        self.name = name
        self.age = age
        
    # Method to display student details
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
# Create an object and pass values to the constructor
s1 = Student("Shiv", 20)
s2 = Student("Om", 20)

# Display student details
s1.display()
s2.display()

    
    