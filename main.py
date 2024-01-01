import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
i = 0
while i < 5:
        print(i)
        i += 1