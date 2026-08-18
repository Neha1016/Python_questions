
# Abstraction means hiding implementation details and showing only the necessary features .
# Python provides abstraction using the abc module .

# Import ABC and abstract method
from abc import ABC, abstractmethod

# Abstract class 
class Animal(ABC):
    
    # Abstract method
    # child classes must provide its implementation
    @abstractmethod
    def sound(self):
        pass
     
 # Child class
class Dog(Animal):
        
    # Implementation the abstract method
    def sound(self):
        print("Dog barks")
            
 # Create object of Dog
d = Dog ()
    
# Call the implementation method
d.sound()