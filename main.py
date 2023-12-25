import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
i = 0
while i < 5:
        print(i)
        i += 1