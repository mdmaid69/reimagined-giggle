import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def find_common_elements(list1, list2):
        return set(list1) & set(list2)