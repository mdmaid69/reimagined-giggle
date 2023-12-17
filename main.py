import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def convert_to_octal(n):
        return oct(n)