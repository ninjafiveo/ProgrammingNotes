class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Constructor
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.save_dog_info()  # Calls save_dog_info method when a new Dog object is created

    # Method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def zoomies(self):
        return f"{self.name} runs in circles like crazy!"
    
    def dog_math(self, num1, num2):
        answer = num1 + num2
        return f"{num1} + {num2} = snack time for {self.name} and {answer} for hoomans."
    
    def save_dog_info(self):
        with open("doggos.txt", "a") as file:
            file.write(f"{self.name}, {self.age}, {self.species}, {self.breed}\n")
    
    

# Creating objects of the class Dog
dog1 = Dog("Buddy", 8, "Golden Retriever")
dog2 = Dog("Mozzy", 4, "Multipoo")
dog3 = Dog("Ralph", 2, "Beagle")

# Accessing attributes and calling methods
print(dog1.name)     # Outputs: Buddy
print(dog2.age)      # Outputs: 5
print(dog1.bark())   # Outputs: Buddy says Woof!
print(dog2.dog_math(3, 9)) # Ouputs: 3 + 9 = snack time for Mozzy and 12 for hoomans.
print(dog3.dog_math(7, 35)) # Ouputs: 7 + 35 = snack time for Mozzy and 42 for hoomans.






