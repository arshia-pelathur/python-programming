class Animal:
    species = "Generic Animal"

    def __init__(self, name):
        self.name = name
        self.sound = "Generic Sound"

class Dog(Animal):
    species = "Canine"

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        self.sound = 'bark'

# Accessing class variables
print(Animal.species)  # Output: Generic Animal
print(Dog.species)     # Output: Canine

# Creating instances
animal_instance = Animal("Generic")
dog_instance = Dog("Rover", "Golden Retriever")

# Accessing instance variables
print(animal_instance.name)  # Output: Generic
print(animal_instance.sound) 
print(dog_instance.name)     # Output: Rover
print(dog_instance.breed)    # Output: Golden Retriever
print(dog_instance.sound)  


# Accessing class variables through instances
print(animal_instance.species)  # Output: Generic Animal
print(dog_instance.species)     # Output: Canine
print(animal_instance.__dict__)

# Modifying class variable in an instance
animal_instance.species = "Modified in animal_instance"
print(animal_instance.species)  # Output: Modified in animal_instance
print(Animal.species)           # Output: Generic Animal
print()


# Modifying class variable directly in the class
Animal.species = "Modified in Animal class"
print(Animal.species)           # Output: Modified in Animal class
print(animal_instance.species)  # Output: Modified in animal_instance (this is an instance variable now)
print(dog_instance.species)     # Output: Canine (Dog's own class variable)

print(animal_instance.__dict__)

# Adding a new class variable to Dog
Dog.species = "Modified in Dog class"
print(Dog.species)              # Output: Modified in Dog class
print(dog_instance.species)     # Output: Modified in Dog class
print(Animal.species)           # Output: Modified in Animal class
print(animal_instance.species)  # Output: Modified in animal_instance
