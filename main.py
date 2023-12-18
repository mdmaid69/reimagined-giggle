import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)