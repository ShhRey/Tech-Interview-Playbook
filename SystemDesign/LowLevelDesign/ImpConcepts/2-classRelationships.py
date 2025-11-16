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
It models a "has-a" relationship between a whole and its parts; but unlike Aggregation, it signifies strong ownership and lifecycle dependency. 
The contained object (part) cannot exist independently. Composition is the strongest form of Association.


Key Characteristics:
- The whole owns the part and controls its lifecycle.
- When the whole is destroyed, the parts are also destroyed.
- The parts are not shared with any other object.
- The part has no independent meaning or identity outside the whole.

UML Diagram Representation:
- Composition is represented by a filled diamond (◆) at the “whole” end of the relationship.
It is a preferred alternative to inheritance when building flexible systems.

When to use Composition?
- The part is not meaningful without the whole.
- The whole should control the lifecycle of its parts.
- The parts are not reused elsewhere in the system.
- You want to model a strong containment relationship.

Best Practices for Composition
- You can build complex behavior by composing smaller, reusable parts.
- It avoids the tight coupling and fragility of inheritance hierarchies.
- You can swap out parts dynamically to modify behavior.
'''

# Engine is created inside Car
# This way Engine will not Exist without Car
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

# Car controls the lifestyle for Engine
class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower) 

    def show_specs(self):
        print(f"{self.model} has {self.engine.horsepower} HP")





'''
#============================================================================== 4. Dependency ========================================================================#
Unlike Association, Aggregation, or Composition, Dependency is not structural. It does not imply a long-term relationship or shared lifecycle. 
The dependent class does not store the other class as an attribute. Instead, it reflects a one-time interaction, often through method parameters, local variables, or return types.
It describes a "uses-a" relationship where one class temporarily uses another class to perform a task. 

Key Characteristics:
- Short-lived: The relationship exists only during method execution.
- No ownership: The dependent class does not store the other as a field.

UML Diagram Representation:
- Dependency is shown using a dashed arrow (--->) pointing from the dependent class to the class it depends on.

When to use Dependency?
- You want loose coupling.
- You only need the object temporarily.
- You want to keep the class lightweight.

Best Practices for Dependency
- A class accepts another class as a method parameter.
- A class instantiates or uses another class inside a method.
- A class returns an object of another class from a method.
- Avoid storing it as an attribute.
- Use dependency injection for flexibility.


Dependencies can appear in several common forms within a class:
1. As Method Parameters: The dependency is passed into a method only when needed.
2. As Class Fields/Instance Variables: The dependency is held as a field, often for repeated use.
3. As Constructor Parameters: The dependency is provided when the object is created. 
This is the foundation for Dependency Injection and is highly preferred.


What is Dependency Injection?
Dependency Injection is a design technique where a class receives the objects it depends on, instead of creating them itself.
This leads to:
- Better testability: You can inject mock dependencies during unit tests.
- Greater modularity: Swap implementations (e.g., EmailSender → SMSSender) without changing core logic.
- Loose coupling: Classes only depend on abstract contracts (interfaces), not concrete implementations.
'''

# Dependency (Mechanic uses Car temporarily to perform repair)
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

class CarWash:
    def clean(self, car):
        print(f"Washing the {car.color} {car.model}... Sparkling clean!")

class Mechanic:
    def repair(self, car):
        print(f"Repairing {car.model}... Done!")