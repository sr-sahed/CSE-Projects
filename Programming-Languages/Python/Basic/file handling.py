# Write to a file
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# Read from a file
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
