import itertools
print(list(itertools.permutations([1, 2, 3])))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))