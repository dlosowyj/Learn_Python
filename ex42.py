## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # Set the object's name to the given name
        self.name = name

# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Set the object's name to the given name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Set the object's name to the given name
        self.name = name

        # Set the object's pet to None, for now
        self.pet = None

# Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        # This calls the __init__ of Person
        super(Employee, self).__init__(name)

        # Set the object's salary to the given salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is a Person
mary = Person("Mary")

# Set mary's pet to be satan
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# Set frank's pet to rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
