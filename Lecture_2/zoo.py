from animals import *

class Zoo(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animals = []
        self.animal_count = 0

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def add_animal(self, animal:Animal):
        self.animals.append(animal)
        self.animal_count += 1
    
    def get_animals(self) -> Animal:
        return self.animals

    def print_animals(self):
        animals_ = self.get_animals()
        print(f"Zoo {self.name} has: ")
        for animal in animals_:
            print(animal.name, "of", animal.age)

    def __str__(self):
        return f"Zoo {self.name} has total {self.animal_count} animals.\n"