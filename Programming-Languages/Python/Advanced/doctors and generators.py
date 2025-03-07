def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
