import itertools
print(list(itertools.permutations([1, 2, 3])))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)