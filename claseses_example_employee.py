
class Employee:
    company = "Chicken Tacos"

    # Initializer / Constructor
    def  __init__(self, l_name, f_name, id, salary, position):
        self.l_name = l_name
        self.f_name = f_name
        self.id = id
        self.salary = salary
        self.position = position
        self.save_employee_info()

    # Methods
    def do_dishes(self):
        return f"{self.f_name} washes the dishes."

    def serve_tacos(self):
        return f"{self.f_name} delivers the tacos."
    
    def taco_maker(self, taco_type, num_of_tacos):
        return f"{self.f_name} makes {num_of_tacos} {taco_type}."
    
    def save_employee_info(self):
        with open("employee_list.txt","a") as file:
            file.write(f"{self.l_name}, {self.f_name}, {self.id}, {self.salary}, {self.position}\n")

# Create Employees
emp1 = Employee("Smith", "Bob", 1, 30000, "Dishwasher")
emp2 = Employee("Johnson", "Kelly", 2, 55000, "Manager")
emp3 = Employee("Escobar", "Pablo", 3, 350000, "Taco Maker")
emp4 = Employee("Heisenberg", "Warner", 4, 42, "Salsa Maker")

print(emp1.f_name)
print(emp2.do_dishes())
print(emp3.serve_tacos())
print(emp4.taco_maker("Shredded Chicken Diablo Fire", 12))
