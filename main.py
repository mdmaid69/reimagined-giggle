import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
n = 10
print("Square numbers:", [x**2 for x in range(n)])