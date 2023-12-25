import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)