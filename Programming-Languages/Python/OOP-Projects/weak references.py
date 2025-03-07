import weakref

class Person:
    pass

obj = Person()
weak_obj = weakref.ref(obj)  # Weak reference

print(weak_obj())  # Output: <__main__.Person object>
del obj
print(weak_obj())  # Output: None
