import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))