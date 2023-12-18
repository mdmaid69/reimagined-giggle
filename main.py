import itertools
print(list(itertools.permutations([1, 2, 3])))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)