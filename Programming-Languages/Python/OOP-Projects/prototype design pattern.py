import copy

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

car1 = Car("Tesla", "Red")
car2 = car1.clone()
car2.color = "Blue"

print(car1.color, car2.color)  # Output: Red Blue
