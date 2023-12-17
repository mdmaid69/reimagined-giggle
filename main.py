import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
print(sum(range(10)))