from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda x, y: x + y, nums)

print(squared, evens, sum_all)  # Output: [1, 4, 9, 16, 25] [2, 4] 15
