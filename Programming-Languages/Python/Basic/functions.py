# Regular Function
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# Lambda Function
square = lambda x: x ** 2
print(square(5))

# *args & **kwargs
def add(*numbers):
    return sum(numbers)
print(add(1, 2, 3, 4))
