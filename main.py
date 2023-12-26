import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)