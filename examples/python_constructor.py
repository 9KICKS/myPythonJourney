class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This is the destructor:
#    def __delete__(self):
#        print(f"{self.name} is dead")

# This is the string representation:
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def talk(self):
        print(f"{self.name} says hello")

    def walk(self):
        print(f"{self.name} walked")

    def birthday(self):
        self.age += 1


fola = Human("Folahan", 3)
print(fola)
