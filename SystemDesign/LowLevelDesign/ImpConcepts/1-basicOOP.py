# Simple Illustration for OOP Concepts in Python

# Parent Class
class Car:
    # __init__ is a special method (Initializer) called constructor
    #  Gets automatically called when a new class is created
    def __init__(self, maker: str, model: str, year: int):
        # self is the actual instance of the class
        # Other attributes/properties of the object
        self.maker = maker
        self.model = model
        self.year = year
        # Defining a Default Attribute; Setting it to Private
        self.__isRunning = False

    # Other Methods/Behaviours of the Class
    def start_engine(self):
        print(f"The {self.maker} {self.model}'s engine is starting.")
        self.__isRunning = True

    def stop_engine(self):
        print(f"The {self.maker} {self.model}'s engine is stopping.")
        self.__isRunning = False

    
    # Generic Method that will be Overridden
    def fuel_up(self):
        raise NotImplementedError("This method must be implemented by a sub-class!")


    # Private Attribute can only be Accessed via Method
    # Good practise to start method name as get_ 
    def get_status(self):
        return "Yes" if self.__isRunning == True else "No"


#1 Child Class
class ElectricCar(Car):
    def __init__(self, maker: str, model: str, year: int, battery_life: int):
        # Calling Parent Class Constructor and Inheriting its Attributes
        super().__init__(maker, model, year)
        # Adding New Attribute of Child Class
        self.battery_life = battery_life

    # New Method for Child Class
    def charged(self):
        print("The Electric Car has finished charging.")

    # Overriding Method => Polymorphism
    def fuel_up(self):
        print(f"The {self.maker} {self.model} is getting recharged.")

#2 Child Class
class FuelCar(Car):
    # Calling Parent Class Constructor and Inheriting its Attributes
    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)

    # Overriding Method => Polymorphism
    def fuel_up(self):
        print(f"The {self.maker} {self.model} is getting refueled.")



# Creating Objects/Instances of the Class
car1 = Car("Honda", "Civic", 2022)
car2 = Car("Toyota", "Corolla", 2018)

ecar1 = ElectricCar("Tesla", "Model S", 2024, 100)


# Accessing attributes and calling methods on the objects
print(f"Car 1 is a {car1.year} made {car1.maker} {car1.model}.")





'''
#============================================================================== 1. Implementing Abstraction ========================================================================#
It is the concept of showing only essential/relevant high-level functionality and hiding complex internal implementation details. It focuses on "what" and not the "how".
Abstraction is about creating a simplified view of a system that highlights the essential features while suppressing the irrelevant details.

- Reduces Complexity: Users and developers don't need to understand the internal machinery—just the interface.
- Improves Usability: A clean, minimal surface area makes your classes easier to learn and use correctly.
- Enables Reusability and Substitutability: Well-abstracted components can be swapped or extended with minimal changes.
'''
# When you call car1.start_engine() you dont need to know how the method is implemented internally, you just know that calling this method will start the car's engine!
# This will work because it's a Public Method
car1.start_engine()




'''
#======================================================================================== 2. Implementing Encapsulation ================================================================================#
#============================================================================== Encapsulation = Data Hiding + Controlled Access ========================================================================#
It is the concept of hiding implementation details of an object and only exposing necessary information through public methods. You can create private attributes and methods using (__)
It helps you build systems that are robust, secure, and easy to maintain.

- Data Hiding: By restricting direct access to internal fields, encapsulation shields sensitive data from unintended interference or misuse.
- Controlled Access and Security: : It ensures that data can only be accessed or modified through well-defined methods, allowing you to enforce rules, validation, or logging when needed.
- Improved Maintainability: Because internal implementation details are hidden, you can refactor or optimize them without affecting the external code that depends on the class.

'''
# Trying to access the Private Attribute directly will fail
# This will raise an AttributeError
# print(car1.__is_running) 

# Instead, we create a Public Method to get the Status
print(f"Is the car running? {car1.get_status()}")



'''
#============================================================================== 3. Implementing Inheritance ========================================================================#
It is the concept where a new Child Class inherits the properties/attributes and behaviours/methods from an existing Parent Class.
It promotes Code Resusability and Logical Hierarchy.

- Code Reusability: Common logic is written once in the parent class and inherited by all child classes, reducing duplication.
- Logical Hierarchy: Inheritance models real-world “is-a” relationships, such as ElectricCar is a Car or Admin is a User.
- Ease of Maintenance: Changes to shared behavior only need to be made in one place (the superclass) and all subclasses benefit automatically.
'''
# Creating Object for Child Class 
print(f"The {ecar1.maker} {ecar1.model} has a battery life of {ecar1.battery_life} miles.")
ecar1.charged()



'''
#============================================================================== 4. Implementing Polymorphism ========================================================================#
It allows objects of different classes to be treated as objects of a common superclass. This is often achieved by having methods with the same name in different classes that perform different tasks.
It lets you call the same method on different objects, and have each object respond in its own way.


- Encourages loose coupling: You interact with abstractions (interfaces or base classes), not specific implementations.
- Enhances flexibility: You can introduce new behaviors without modifying existing code, supporting the Open/Closed Principle.
- Promotes scalability: Systems can grow to support more features with minimal impact on existing code.
'''
# Create a list of different car objects
vehicles = [ElectricCar("Tesla", "Model 3", 2023, 100), FuelCar("Ford", "Mustang", 2024)]
for vehicle in vehicles:
    vehicle.fuel_up()