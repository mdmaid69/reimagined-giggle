import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)