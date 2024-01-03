def is_even(n):
        return n % 2 == 0
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))