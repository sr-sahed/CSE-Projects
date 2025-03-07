class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"This is class {cls.__name__}"

print(Math.add(5, 10))  # Output: 15
print(Math.info())  # Output: This is class Math
