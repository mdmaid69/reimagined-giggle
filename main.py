numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))