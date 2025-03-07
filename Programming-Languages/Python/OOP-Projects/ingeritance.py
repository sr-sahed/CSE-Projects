class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):  
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak(), cat.speak())  # Output: Woof! Meow!
