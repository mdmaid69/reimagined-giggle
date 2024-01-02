import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def convert_to_hex(n):
        return hex(n)