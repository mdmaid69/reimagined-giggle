def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))