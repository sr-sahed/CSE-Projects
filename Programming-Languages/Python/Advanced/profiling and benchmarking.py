import timeit

code = "sum(range(1000))"
execution_time = timeit.timeit(code, number=1000)
print("Execution Time:", execution_time)
