def square_number(x):
        return x**2
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))