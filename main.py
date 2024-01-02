n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))