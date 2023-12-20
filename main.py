import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])