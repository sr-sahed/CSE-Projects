from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Class
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!
