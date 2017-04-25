## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def make_noise(self):
        pass

# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # Set the object's name to the given name
        self.name = name

    def make_noise(self):
        print("Bark!")

# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Set the object's name to the given name
        self.name = name

    def make_noise(self):
        print("I'm a destructive jerk.")

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
class Fish(Animal):
    
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        print("Blub!")

# Salmon is-a fish
class Salmon(Fish):
    
    def __init__(self, name, size):
        super(Salmon, self).__init__(name)

        self.size = size

# Halibut is-a fish
class Halibut(Fish):
    
    def __init__(self, name, weight):
        super(Halibut, self).__init__(name)

        self.weight = weight

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
flipper = Fish("Flipper")

# crouse is-a Salmon
crouse = Salmon("Crouse", 12)

# harry is-a Halibut
harry = Halibut("Harry", 0.5)

rover.make_noise()
satan.make_noise()
mary.pet.make_noise()
flipper.make_noise()
print(crouse.size)
print(harry.weight)
