import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)