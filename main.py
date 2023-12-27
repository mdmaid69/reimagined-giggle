n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))