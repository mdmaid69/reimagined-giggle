import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def reverse_list(lst):
        return lst[::-1]