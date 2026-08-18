# Polymorphism means one method/name can behave differently for different objects.

# Parent class
class Animal:
    
    # Common method
    def sound(self):
        print("Animal makes a sound")
        
# Child class inherits from Animal
class Dog(Animal):
    
    # Override the parent method
    def sound(self):
        print("Dog can bark")
        
# Another child class
class Cat(Animal):
    
    # Override the parent method
    def sound(self):
        print("Cat Meows")
        
        

# create objects
d = Dog()
c = Cat()

# Same method name gives different result
d.sound()
c.sound()