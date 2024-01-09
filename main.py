import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def find_difference(list1, list2):
        return set(list1) - set(list2)