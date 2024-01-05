import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b