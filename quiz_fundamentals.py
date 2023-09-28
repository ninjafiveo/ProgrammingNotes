intro = "Hello World"
print(intro)

first_name = input("What is your first name?  ")
print(first_name)

age = 87
temperature = 98.7
too_hot = False

print(type(age))
print(type(temperature))
print(type(too_hot))

add = age + temperature
subtraction = age - temperature
multiplication = age * temperature
division = age / temperature
square = age ** temperature
print(add)
print(subtraction)
print(multiplication)
print(division)
print(square)

print(intro + first_name)
print(f"{intro}, {first_name}")
