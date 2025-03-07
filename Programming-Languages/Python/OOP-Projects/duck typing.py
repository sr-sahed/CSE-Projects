class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())  # Output: Meow
animal_sound(Dog())  # Output: Woof
