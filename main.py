def calculate_average(lst):
        return sum(lst) / len(lst)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))