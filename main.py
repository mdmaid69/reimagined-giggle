import itertools
print(list(itertools.permutations([1, 2, 3])))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b