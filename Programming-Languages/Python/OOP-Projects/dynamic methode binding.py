class Dynamic:
    pass

def new_method():
    return "I am dynamically added!"

obj = Dynamic()
obj.method = new_method  # Adding method dynamically
print(obj.method())  # Output: I am dynamically added!
