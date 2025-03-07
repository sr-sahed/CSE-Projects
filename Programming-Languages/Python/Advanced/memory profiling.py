from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)]
    return sum(a)

my_function()
