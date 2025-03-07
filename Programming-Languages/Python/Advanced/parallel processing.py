from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = executor.map(task, range(5))

print(list(results))
