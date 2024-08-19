class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

dog1 = Dog("Buddy", 3)
print(f"{dog1.name} is {dog1.age} years old.")
print(dog1.bark())
