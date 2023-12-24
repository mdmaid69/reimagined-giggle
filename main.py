import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))