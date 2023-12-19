def find_min(numbers):
        return min(numbers)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))