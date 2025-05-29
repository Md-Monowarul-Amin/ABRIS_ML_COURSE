from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    @abstractmethod
    def move(self):
        pass

    def __str__(self):
        return f"Animal {self.name} of age {self.age}"
    

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def move(self):
        return "I can run."


class Fish(Animal):
    def __init__(self, name, age, number_of_fins):
        super().__init__(name, age)
        self.number_of_fins = number_of_fins
    
    def move(self):
        return "I can swim"


class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.wings = 2
        self.color = color
    
    def move(self):
        return "I can fly."


b = Bird("Pigeon", 1, "White")
print(b.get_name())
print(b.move())

