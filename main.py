import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
from collections import Counter
print(Counter("hello world"))