import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
n = 10
print("Powers of 2:", [2**x for x in range(n)])