import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def sort_numbers(numbers):
        return sorted(numbers)