from abc import ABC, abstractmethod

#  ABSTRACTION

# ABC means Abstract Base Class
# We cannot directly create an object of this class.

class Person(ABC):

    def __init__(self, name, age):
        
        #  CONSTRUCTOR
        # __init__() is called automatically when an object is created .
        self.name = name
        self.age = age

    # Abstract method
    # Child classes MUST implement this method.
    @abstractmethod
    def show_role(self):
        pass


#  INHERITANCE


# Student inherits from Person
class Student(Person):

    def __init__(self, name, age, marks):
        
        # super() calls the constructor of the parent class
        super().__init__(name, age)

        #  ENCAPSULATION

        # __marks is a private variable.
        self.__marks = marks

    # Getter method
    # Used to access private data.
    def get_marks(self):
        return self.__marks

    # Setter method
    # Used to change private data safely.
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")

    # Implementation of abstract method
    def show_role(self):
        print("Role: Student")

    # Normal method
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.__marks)

#  POLYMORPHISM

class Teacher(Person):

    # Teacher also implements the same method
    # but gives different output.
    def show_role(self):
        print("Role: Teacher")

#  OBJECT CREATION

# Creating Student object
student = Student("Shivay", 20, 85)

# Calling methods
student.show_role()
student.show_details()

print("\nMarks:", student.get_marks())


# Changing private data using setter
student.set_marks(90)

print("Updated Marks:", student.get_marks())


# Creating Teacher object
teacher = Teacher("Priya", 35)

teacher.show_role()



# POLYMORPHISM EXAMPLE

# Same method name -> different behavior
people = [student, teacher]

for person in people:
    person.show_role()