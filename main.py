import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)