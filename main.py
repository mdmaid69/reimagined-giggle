import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def get_array_from_file(filename, typecode):
        a = array.array(typecode)
        with open(filename, "rb") as f:
        a.fromfile(f, os.path.getsize(filename) // a.itemsize)
        return a