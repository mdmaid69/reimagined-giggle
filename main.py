import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def remove_duplicates(lst):
        return list(set(lst))