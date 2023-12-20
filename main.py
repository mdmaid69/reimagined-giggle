import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])