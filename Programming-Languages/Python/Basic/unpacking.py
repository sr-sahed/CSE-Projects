# List Unpacking
numbers = [1, 2, 3]
a, b, c = numbers
print(a, b, c)

# Dictionary Unpacking
person = {"name": "Bob", "age": 30}
print(**person)  # Output: name=Bob age=30
