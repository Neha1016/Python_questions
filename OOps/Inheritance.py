# Inheritance allows one class to use the properties and methods of another class 

# Parent class
class Animal:
    
    # Method of parent class
    def eat(self):
        print("Animal can eat")
        
# Child class inherits from Animal
class Dog(Animal):
    
    #Method of child class
    def bark(self):
        print("Dog can bark")
        
# Create object of child class
d = Dog()

# Child object can use parent class method 
d.eat()

# Child object can use its own method 
d.bark()