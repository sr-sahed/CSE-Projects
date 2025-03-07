class Box:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, other):  # Overloading `+` operator
        return Box(self.volume + other.volume)

box1 = Box(10)
box2 = Box(20)
result = box1 + box2  # Calls __add__
print(result.volume)  # Output: 30
