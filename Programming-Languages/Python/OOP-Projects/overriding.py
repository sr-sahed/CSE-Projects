class Shape:
    def area(self):
        return "Calculating area"

class Circle(Shape):
    def area(self):
        return "πr²"

class Square(Shape):
    def area(self):
        return "side²"

shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.area())  
# Output:
# πr²
# side²
