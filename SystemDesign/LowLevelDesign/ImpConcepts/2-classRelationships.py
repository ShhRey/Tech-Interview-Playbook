# Why Class Relationships matter?
# They shape how your objects collaborate, how they depend on each other, and ultimately, how robust and adaptable your systems are. 
# Choosing the right relationship improves code readability, testability, and maintainability.

'''
#============================================================================== 1. Association ========================================================================#
It describes a relationship where one class uses, communicates or otherwise connects to another class. The objects may interact frequently, but remain independent;
Does one object need to know about the existence of another object to perform its responsibilities? If the answer is YES, there is Association between them.

Direction (who knows about whom):
- Unidirectional: Only one class has attribute reference to the other.
- Bidirectional: Both classes have references to each other.

Multiplicity (how many objects connected):
- OneToOne: Each object is associated with exactly one object of the other class                        (Car might be associated with one type: Electronic)
- OneToMany: One object can be associated with many other objects                                       (Driver might be associated with many Cars)
- ManytoMany: Objects from both classes can be associated with multiple objects from the other          (Mechanic can be associated to many Cars, One Car can be associated with many Mechanics)

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