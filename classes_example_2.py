# Create a dog class

class Dog:
    #class attribute
    species = "Canis familiaris"

    # Initializer / Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Methods (AKA Functions inside a class)
    def bark(self):
        return f"{self.name} says Woof!"
    
    def zoomie(self):
        return f"{self.name} runs in circles like they're crazy."
    
    def dog_math(self, num1, num2):
        answer = num1 + num2
        return f"{num1} + {num2} = snack time for {self.name}, and {answer} for hoomans."

# Creating objects for the Dog Class
dog1 = Dog("Mozzy", 4, "Multipoo")
dog2 = Dog("Ralph", 8, "Golden Retreiver")

# Access attributes of the class.
print(dog1.name)
print(dog1.breed)
print(dog2.name)
print(dog2.bark())
print(dog1.dog_math(3, 12))