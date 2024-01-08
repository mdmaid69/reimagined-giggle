numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))