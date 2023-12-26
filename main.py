import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])