import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
name = "Python"
print("Hello,", name)