# Lab: The Galactic Data Manager
#! 1. Defining the Starship class:
class Starship:
    def __init__(self, name, model, role, crew_size):
        self.name = name
        self.model = model
        self.role = role
        self.crew_size = crew_size
        
#! Step 2: Creating and Using Methods in the Starship Class
    def get_info(self):
        return f"Starship: {self.name}\nModel: {self.model}\nRole: {self.role}\nCrew Size: {self.crew_size}\n"
    
    def to_dict(self):
        return {
            "name": self.name,
            "model": self.model,
            "role": self.role,
            "crew_size": self.crew_size
        }

#! 3. Defining the GalacticDataManager class:
class GalacticDataManager:
    def __init__(self):
        self.data = {}

    def add_starship(self, starship):
        self.data[starship.name] = starship.to_dict()
    
    def display_all_starships(self):
        for starship_name, starship_data in self.data.items():
            print(f"{starship_name}:")
            for attribute, value in starship_data.items():
                print(f"    {attribute.capitalize()}: {value}")
            print("\n")

#! 4. Testing the Classes:
# Creating instances of Starship
millennium_falcon = Starship("Millennium Falcon", "YT-1300F", "Freighter", 4)
star_destroyer = Starship("Star Destroyer", "Imperial I-class", "Destroyer", 37000)

# Instantiating the GalacticDataManager and adding starships to it
galactic_data_manager = GalacticDataManager()
galactic_data_manager.add_starship(millennium_falcon)
galactic_data_manager.add_starship(star_destroyer)

# Displaying all starships and their information
galactic_data_manager.display_all_starships()

