def add_numbers(a, b):
        return a + b
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))