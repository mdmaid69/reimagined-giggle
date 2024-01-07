import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b