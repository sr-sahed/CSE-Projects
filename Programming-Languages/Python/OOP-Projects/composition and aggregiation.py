class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        return self.engine.start() + " & Car is moving!"

car = Car()
print(car.start())  # Output: Engine started & Car is moving!
