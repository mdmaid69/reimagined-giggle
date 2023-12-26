import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def find_union(list1, list2):
        return set(list1) | set(list2)