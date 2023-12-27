import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
n = 10
print("Powers of 2:", [2**x for x in range(n)])