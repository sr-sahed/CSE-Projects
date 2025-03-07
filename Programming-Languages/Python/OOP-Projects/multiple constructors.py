class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p1 = Person("Alice", 25)
p2 = Person.from_string("Bob-30")
print(p2.name, p2.age)  # Output: Bob 30
