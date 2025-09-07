# Why Class Relationships matter?
# They shape how your objects collaborate, how they depend on each other, and ultimately, how robust and adaptable your systems are. 
# Choosing the right relationship improves code readability, testability, and maintainability.

'''
#============================================================================== 1. Association ========================================================================#
It describes a relationship where one class uses, communicates or otherwise connects to another class. The objects may interact frequently, but remain independent;
Does one object need to know about the existence of another object to perform its responsibilities? If the answer is YES, there is Association between them.

Direction (who knows about whom):
- Unidirectional: Only one class has reference to the other.
- Bidirectional: Both classes know about each other.

Multiplicity (how many objects connected):
- OneToOne: Each object is associated with exactly one object of the other class
- OneToMany: One object can be associated with many other objects
- ManytoMany: Objects from both classes can be associated with multiple objects from the other

When to use Association?
- Two classes need to collaborate.
- One class needs to send a message to or query another.
- You want to express relationships without implying ownership.
- You need flexibility, both objects should be reusable and independently manageable.

Best Practices for Association
- Two classes need to collaborate.
- One class needs to send a message or query to another.
- You want to express relationships without implying ownership.
- Clearly document multiplicity and direction.
'''
# Unidirectional Association (Car has a Driver, Driver does not know about Car)
class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, driver):
        # Car has-a Driver
        self.driver = driver  

    def drive(self):
        print(f"{self.driver} is driving the car.")


# Bidirectional Association (Author writes multiple Books, Each Book knows it Author)
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        # Set the reverse association
        book.set_author(self)

class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def set_author(self, author):
        self.author = author



'''
#============================================================================== 2. Aggregation ========================================================================#
It represents "has-a" relationship between two classes where one class (Whole) groups or organizes other classes (Part), but does not control their lifecycle (ie they can exist independently).
It is a specialized form of Association.
 
Direction (who knows about whom):
- 

Multiplicity (how many objects connected):
- 

When to use Aggregation?
- 
- 
- 
- 

Best Practices for Aggregation
- 
- 
- 
'''





'''
#============================================================================== 3. Composition ========================================================================#


 
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