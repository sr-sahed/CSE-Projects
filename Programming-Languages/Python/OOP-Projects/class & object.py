class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Instance Variable
        self.age = age

    def introduce(self):  # Method
        return f"My name is {self.name} and I am {self.age} years old."

# Object Creation
p1 = Person("Alice", 25)
print(p1.introduce())  # Output: My name is Alice and I am 25 years old.
