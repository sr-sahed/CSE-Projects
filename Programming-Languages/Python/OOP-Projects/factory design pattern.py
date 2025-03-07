class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        animals = {"dog": Dog, "cat": Cat}
        return animals.get(animal_type, Dog)()

animal = AnimalFactory.get_animal("cat")
print(animal.speak())  # Output: Meow
