from zoo import Zoo
from animals import *


print("Create your own zoo.")
zoo_name = input("Enter the name of the zoo: ")
zoo_location = input("Enter the location of the zoo: ")

zoo_ = Zoo(zoo_name, zoo_location)

def input_cat():
    name = input("Enter cat name: ")
    age = input("Enter cat age: ")
    color = input("Enter cat color: ")

    return name, age, color

def input_fish():
    name = input("Enter fish name: ")
    age = input("Enter fish age: ")
    wings = input("Enter fish wings: ")

    return name, age, wings

def input_bird():
    name = input("Enter bird name: ")
    age = input("Enter bird age: ")
    color = input("Enter bird color: ")

    return name, age, color


while True:
    print("Press 1 to add a cat.")
    print("Press 2 to add a fish.")
    print("Press 3 to add a bird.")
    print("Press 5 to exit() ")

    n = int(input("Enter the number: "))
    if n == 1:
        name, age, color = input_cat()
        cat_ = Cat(name, age, color)
        zoo_.add_animal(cat_)

    elif n == 2:
        name, age, wings = input_fish()
        fish_ = Fish(name, age, wings)
        zoo_.add_animal(fish_)

    elif n == 3:
        name, age, color = input_bird()
        bird_ = Bird(name, age, color)
        zoo_.add_animal(bird_)
    
    elif n == 5:
        break

    else:
        continue


print(zoo_.print_animals())

# fish_1 = Fish("Salmon", 1, 4)
# print(fish_1)
# print(fish_1.get_name())
# print(fish_1.move())