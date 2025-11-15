# Why Class Relationships matter?
# They shape how your objects collaborate, how they depend on each other, and ultimately, how robust and adaptable your systems are. 
# Choosing the right relationship improves code readability, testability, and maintainability.

'''
#============================================================================== 1. Association ========================================================================#
It describes a relationship where one class uses, communicates or otherwise connects to another class. The objects may interact frequently, but remain independent;
Does one object need to know about the existence of another object to perform its responsibilities? If the answer is YES, there is Association between them.

Key Characteristics:
- Association reflects a "has-a" or "uses-a" relationship.
- Associated objects are loosely coupled and can exist independently of one another.

UML Diagram Representation:
- Solid line: Represents an association between classes.
- Arrowhead (->): Indicates unidirectionality (who knows whom).
- Double Arrowheads (<-->): Implies a bidirectional association.

Types of Association:
Based on Direction (who knows about whom):
- Unidirectional: Only one class has attribute reference to the other.
- Bidirectional: Both classes have references to each other.

Based on Multiplicity (how many objects connected):
- OneToOne (--): Each object is associated with exactly one object of the other class                        (Car might be associated with one type: Electronic)
- OneToMany (-->): One object can be associated with many other objects                                      (Driver might be associated with many Cars)
- ManytoMany (<-->): Objects from both classes can be associated with multiple objects from the other        (Mechanic can be associated to many Cars, One Car can be associated with many Mechanics)

When to use Association?
- Two classes need to collaborate.
- One class needs to call methods on an instance of another class.
- You want to express relationships without implying ownership or a shared lifecycle.
- You need flexibility, as both objects can be managed, created, and destroyed independently.

Best Practices for Association
- Favour Unidirectional approach, Bidirectional adds complexity and tight coupling, making it harder to maintain code.
- Clearly define multiplicity and enforce it if necessary.
- Use clear attribute names to define relationships.
- Pass the associated object as a parameter to the constructor or a method, rather than creating it inside the class.
'''

# Unidirectional Association (Car has-a Driver, Driver does not know about Car)
class Driver:
    def __init__(self, name):
        self.name = name
        return self.name

class Car:
    def __init__(self, driver):
        # Car has-a Driver
        # It is not created, just passed from Driver
        self.driver = driver  

    def drive(self):
        print(f"{self.driver} is driving the car.")


# Bidirectional Association (Author writes multiple Books, Each Book knows its Author)
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    # Author has Books
    def add_book(self, book):
        self.books.append(book)
        # When book is added, assoc. respective Author
        book.set_author(self)

class Book:
    def __init__(self, title):
        self.title = title
        self.author = None
    
    # Book has-a Author
    def set_author(self, author):
        # It is not created, just passed from Author
        self.author = author



'''
#============================================================================== 2. Aggregation ========================================================================#
It is a weaker form of the whole-part relationship where one class (Whole) groups or organizes other classes (Part), but does not control their lifecycle (ie they can exist independently).
It's often described as a “has-a” relationship with loose ownership (specialized form of Association).
If a class contains other classes for logical grouping only without lifecycle ownership, it is an aggregation.

Key Characteristics:
- The whole and the part are logically connected.
- The whole does not own the part.
- The part can be shared among multiple wholes.
- Both whole and part can be created and destroyed independently.

UML Diagram Representation:
- Aggregation is represented by a hollow diamond (◊) on the “whole” side of the relationship.
The diamond connects to the class that contains or references the other objects.

When to use Aggregation?
- You want to model a whole-part relationship.
- The part can exist independently of the whole.
- You want to reuse the part elsewhere.

Best Practices for Aggregation
- Use lists or collections to represent multiple parts.
- Avoid tight coupling; parts should not depend on the container.
- Pass parts into the container, don't create them inside.
'''

# Aggregation (Garage has many Cars, Cars can exist independently)
class Car:
    def __init__(self, model):
        self.model = model

class Garage:
    def __init__(self):
        # Garage has-a list of Cars
        self.cars = []  

    def add_car(self, car):
        # Car is passed in, not created
        self.cars.append(car)  

    def show_cars(self):
        for car in self.cars:
            print(f"Car model: {car.model}")



'''
#============================================================================== 3. Composition ========================================================================#



Key Characteristics:
- 
- 

UML Diagram Representation:
- 
 
Direction (who knows about whom):
- 

Multiplicity (how many objects connected):
- 

When to use Composition?
- 
- 
- 
- 

Best Practices for Composition
- 
- 
- 
'''







'''
#============================================================================== 4. Dependency ========================================================================#



Key Characteristics:
- 
- 

UML Diagram Representation:
- 
 
Direction (who knows about whom):
- 

Multiplicity (how many objects connected):
- 

When to use Dependency?
- 
- 
- 
- 

Best Practices for Dependency
- 
- 
- 
'''