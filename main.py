print([x**2 for x in range(10)])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))