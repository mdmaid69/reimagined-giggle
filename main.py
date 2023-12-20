import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def reverse_string(s):
        return s[::-1]