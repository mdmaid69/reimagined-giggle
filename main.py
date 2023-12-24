import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)