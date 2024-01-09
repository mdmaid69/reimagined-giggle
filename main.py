import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
x = 10
y = 20
print("Sum:", x + y)