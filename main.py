import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])