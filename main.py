import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)