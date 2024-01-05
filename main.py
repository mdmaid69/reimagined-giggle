def calculate_average(lst):
        return sum(lst) / len(lst)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))