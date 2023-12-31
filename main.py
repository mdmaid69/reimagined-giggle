import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)