import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def find_max(numbers):
        return max(numbers)