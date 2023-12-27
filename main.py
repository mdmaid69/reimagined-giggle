import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)