n = 10
print("Square numbers:", [x**2 for x in range(n)])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))