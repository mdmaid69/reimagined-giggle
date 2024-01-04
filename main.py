import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def reverse_list(lst):
        return lst[::-1]