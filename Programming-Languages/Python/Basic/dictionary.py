person = {"name": "Alice", "age": 25}

# Get with default value
print(person.get("city", "Unknown"))  # Output: Unknown

# Check key existence
print("age" in person)  # True

# Iterate over dictionary
for key, value in person.items():
    print(key, ":", value)
