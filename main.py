def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))