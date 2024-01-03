import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])