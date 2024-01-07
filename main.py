import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))